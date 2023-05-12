from bs4 import BeautifulSoup
from decorators.timer import timer

from search.blocks import BaseBlock, Link
from search.page_loader import BasePageLoader
from search.storage import Storage

class Search():
   def __init__(self,
      options,
      pageLoader:BasePageLoader ,
      storage: Storage
   ):
      self.__options = options
      self.__pageLoader = pageLoader
      self.__storage = storage
      self.__failed = False

   @timer
   def run(self):
      opt = self.__options
      page = self.__pageLoader.load(opt.url)

      for block in opt.blocks:
         self.handleBlock(block, page)

   def handleBlock(
         self,
         block: BaseBlock,
         soup: BeautifulSoup
   ):
      selector = block.selector.get()
      elements = soup.select(selector)
      children = block.children

      if (self.__failed): return

      if len(children) <= 0:
         if self.isLimitForKeyExceeded(block.alias) == False:
            self.saveDataByKey(block.alias, elements)
         return

      if len(elements) <= 0:
         print(f"Path:{block.alias} : Не найдено ни одного вхождения")
         print(f"Поиск завершен. Попробуйте поставить задержку между страницами больше")
         self.__failed = True
         return

      for element in elements:
         if type(block) == Link:
            link = element.get("href")
            element = self.__pageLoader.load(link)

         for child in children:
            self.handleBlock(child, element)

   def saveDataByKey(self, key, elements):
      value = "-"
      if len(elements) > 0:
         value = elements[0].text
      self.__storage.add(key, value)

   def isLimitForKeyExceeded(self, key):
      size = self.__storage.size(key)
      print(f"Размер хранилища: {size} Для ключа: {key}")

      if self.__options.limit == -1:
         return False
      
      if size >= self.__options.limit:
         return True

   def getResults(self):
      return self.__storage
   
   def isFailed(self):
      return self.__failed

