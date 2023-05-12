import time

def timer(func):
   def wrapper(*args, **kwargs):
      time_start = time.time()
      value = func(*args, **kwargs)
      time_end = time.time()
      print(f"Elapsed time: {(time_end - time_start):.6f} seconds")
      return value
   return wrapper
