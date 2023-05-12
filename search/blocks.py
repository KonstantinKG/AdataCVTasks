class BaseBlock:
   def __init__(
      self,
      selector,
      alias: str = '',
      children: list = []
   ):
      self.__selector = selector
      self.__alias = alias
      self.__children = children

   @property
   def selector(self):
      return self.__selector

   @property
   def alias(self):
      return self.__alias

   @property
   def children(self):
      return self.__children

class Block(BaseBlock):
   pass

class Link(BaseBlock):
   pass

class EndData(BaseBlock):
   pass