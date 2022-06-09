from threading import Lock, Thread

class Singleton(type):
  
  # def __init__(self):      
  #       if(self._initialized): 
  #         return
  #       self._initialized = True
  #       print ("INIT")
  # _instances = {}
  
  # def __new__(cls, *args, **kwargs):
  #   if cls not in cls._instances:
  #       cls._instances[cls] = super(Singleton, cls).__new__(cls, *args, **kwargs)
  #   return cls._instances[cls]

  _instances = {}

  # _lock: Lock = Lock()

  def __call__(cls, *args, **kwargs):
      # with cls._lock:
        
      if cls not in cls._instances:
        cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
          # instance = super().__call__(*args, **kwargs)
          # cls._instances[cls] = instance
          # cls._instances[cls]._initialized = False
      
      return cls._instances[cls]