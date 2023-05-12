class SearchOptions:
   def __init__(self, url: str, blocks: list, limit:int = -1):
      self.__url = url
      self.__blocks = blocks
      self.__limit = limit

   @property
   def url(self):
      return self.__url

   @property
   def blocks(self):
      return self.__blocks

   @property
   def limit(self):
      return self.__limit