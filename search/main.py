from bs4 import BeautifulSoup
from decorators.timer import timer

from search.blocks import BaseBlock, Link
from search.page_loader import BasePageLoader

class Storage:
   def __init__(self):
      self.__storage = dict()

   def add(self, key, value):
      if key not in self.__storage:
         self.__storage[key] = []
      self.__storage[key].append(value)

   def get(self):
      return self.__storage

class Search():
   def __init__(self,
      options,
      pageLoader:BasePageLoader ,
      storage: Storage
   ):
      self.__options = options
      self.__pageLoader = pageLoader
      self.__storage = storage

   @timer
   def run(self):
      opt = self.__options
      page = self.__pageLoader.load(opt.url)

      for block in opt.blocks:
         self.handleBlock(block, page)

   def getResults(self):
      return self.__storage
   # def handleBlocks(
   #       self,
   #       block: BaseBlock,
   #       soup: BeautifulSoup
   # ):
   #    selector = block.selector.get()
   #    elements = soup.select(selector)

   #    if len(elements) <= 0:
   #       print(f"Path:{block.alias} : Не найдено ни одного вхождения")
   #       self.__pageLoader.failed()

   #    if type(block) == EndData:
   #       if len(elements) > 0:
   #          self.fillStorage(block.alias, elements[0].text)
   #       else:
   #          self.fillStorage(block.alias, "-")
   #       return

   #    for element in elements:
   #       if type(block) == Link:
   #          link = element.get("href")
   #          element = self.__pageLoader.load(link)

   #       for child in block.childrens:
   #          self.handleBlocks(child, element)

   def handleBlock(
         self,
         block: BaseBlock,
         soup: BeautifulSoup
   ):
      selector = block.selector.get()
      elements = soup.select(selector)
      children = block.children

      print(f"Path:{block.alias}")
      if len(children) <= 0:
         self.saveBlock(block, elements)
         return

      if len(elements) <= 0:
         print(f"Path:{block.alias} : Не найдено ни одного вхождения")
         self.__pageLoader.failed()

      for element in elements:
         if type(block) == Link:
            link = element.get("href")
            element = self.__pageLoader.load(link)

         for child in children:
            self.handleBlock(child, element)

   def saveBlock(self, block, elements):
      value = "-"
      if len(elements) > 0:
         value = elements[0].text
      self.__storage.add(block.alias, value)


