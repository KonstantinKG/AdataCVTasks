import re

class BaseSelector:
   def __init__(self, selector : str):
      self.__selector = selector

   def get(self):
      return self.__selector


class Xpath(BaseSelector):
   def get(self):
      return self.__convert_xpath_to_selector()

   def __convert_to_nth_child(self, chunk:str):
      id = chunk.find('[')
      number = int(chunk[id:].replace("[", "").replace("]", ""))
      nth_num = number
      chunk = chunk[:id]
      return f"{chunk}:nth-child({nth_num})"

   def __convert_xpath_to_selector(self):
      chunks = self._selector.split('/')
      regex = "\[([0-9]*)\]"

      new_path = ""
      for chunk in chunks:
         if re.search(regex, chunk):
            chunk = self.__convert_to_nth_child(chunk)
         new_path += f"{chunk} "
      return new_path.strip()

class Selector(BaseSelector):
   pass