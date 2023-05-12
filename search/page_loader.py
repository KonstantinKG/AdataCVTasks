import time
from bs4 import BeautifulSoup
import requests

class BasePageLoader:
   def load(self, url):
      raise NotImplementedError()

class PageLoader(BasePageLoader):
   def __init__(self, delay=0, threshold=3):
      self.__delay = delay

   def load(self, url) -> BeautifulSoup:
      if self.__delay:
         time.sleep(self.__delay)

      page = requests.get(url, verify=False)
      return BeautifulSoup(page.content, "lxml")
