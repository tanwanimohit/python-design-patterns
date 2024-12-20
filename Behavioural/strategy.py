from abc import ABC, abstractmethod

class Lockable(ABC):
    @abstractmethod
    def lock(self):
        raise NotImplementedError
    
    @abstractmethod
    def un_lock(self):
        raise NotImplementedError
    
class Openable(ABC):
    @abstractmethod
    def open(self):
        raise NotImplementedError
    
    @abstractmethod
    def close(self):
        raise NotImplementedError
    
class PasswordLock(Lockable):
    def lock(self):
        print("Password Locked!")
        
    def un_lock(self):
        print("Unlocked with Password")
        
class FingerPrintLock(Lockable):
    def lock(self):
        print("FingerPrint Locked!")
        
    def un_lock(self):
        print("Unlocked with FingerPrint")
        
class KeyCardLock(Lockable):
    def lock(self):
        print("KeyCard Locked!")
        
    def un_lock(self):
        print("Unlocked with KeyCard")
        
class SlidingDoor(Openable):
    def open(self):
        print("Sliding door -> Open")
        
    def close(self):
        print("Sliding door -> closed")
    
class PushDoor(Openable):
    def open(self):
        print("Push door -> Open")
        
    def close(self):
        print("Push door -> closed")
        
class RevolvingDoor(Openable):
    def open(self):
        print("Revolving door -> Open")
        
    def close(self):
        print("Revolving door -> closed")

class Door(ABC):
    _lock_behavior = None
    _open_behavior = None
    
    def set_lock_behavior(self, lock: Lockable):
        self._lock_behavior = lock
        
    def set_open_behavior(self, open: Openable):
        self._open_behavior = open
        
    def lock_door(self):
        self._lock_behavior.lock()
        
    def unlock_door(self):
        self._lock_behavior.un_lock()
        
    def open_door(self):
        self._open_behavior.open()

    def close_door(self):
        self._open_behavior.close()
    
    @abstractmethod
    def get_dimensions(self):
        pass
    
class ClosetDoor(Door):
    
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def get_dimensions(self):
        print(f"{self.height} X {self.width}")
        
class SafeDoor(Door):
    
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def get_dimensions(self):
        print(f"{self.height} X {self.width}")
        
def run():
    closet_door = ClosetDoor(10, 10)
    closet_door.set_lock_behavior(PasswordLock())
    closet_door.set_open_behavior(RevolvingDoor())
    closet_door.lock_door()
    closet_door.unlock_door()
    closet_door.open_door()
    closet_door.close_door()
    closet_door.get_dimensions()

if __name__ == "__main__":
    run()