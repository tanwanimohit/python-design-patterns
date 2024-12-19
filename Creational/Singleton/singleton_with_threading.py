from concurrent.futures import ThreadPoolExecutor
import threading

class Logger:
    _logging = None
    _lock = threading.Lock()
    
    def __init__(self):
        if Logger._logging is not None:
            raise RuntimeError("The instance can't be created again")
        Logger._logging = self
        self.arr = []
    
    @staticmethod
    def get_instance():
        with Logger._lock:
            if Logger._logging is None:
                return Logger()
            return Logger._logging
    
def run_me():
    try:
        logger1 = Logger.get_instance()
        logger1.arr.append(2)
        print(logger1.arr)
    except Exception as e:
        print(e)
    

with ThreadPoolExecutor(max_workers=50) as executor:
    executor.submit(run_me)
    executor.submit(run_me)
