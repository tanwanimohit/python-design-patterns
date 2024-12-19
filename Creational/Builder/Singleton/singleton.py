"""
Singleton Pattern is a creational design pattern 
that guarantees a class has only one instance and provides a global point of access to it.

Use Cases:

Managing Shared Resources (database connections, thread pools, caches, configuration settings)
Coordinating System-Wide Actions (logging, print spoolers, file managers)
Managing State (user session, application state)
"""

class Logger:
    _logging = None
    def __init__(self):
        if Logger._logging is not None:
            raise RuntimeError("The instance can't be created again")
        Logger._logging = self
        self.arr = []
    
    @staticmethod
    def get_instance():
        if Logger._logging is None:
            return Logger()
        return Logger._logging
    
    
logger1 = Logger()

# logger2 = Logger() # Runtime Exception

logger2 = Logger.get_instance()
logger2.arr = [1,2]

print(logger1.arr) # [1, 2]
