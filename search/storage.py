class BaseStorage:
   def add(self, key, value):
      raise NotImplementedError()
   
   def get(self):
      raise NotImplementedError()
   
   def size(self, key):
      raise NotImplementedError()

class Storage:
   def __init__(self):
      self.__storage = dict()

   def add(self, key, value):
      if key not in self.__storage:
         self.__storage[key] = []
      self.__storage[key].append(value)

   def get(self):
      return self.__storage
  
   def size(self, key):
      size = 0
      if key in self.__storage.keys():
         size = len(self.__storage[key])
      return size