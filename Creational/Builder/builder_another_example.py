from abc import ABC, abstractmethod

from enum import Enum

class IphoneColor(Enum):
    RED = "RED"
    BLUE = "BLUE"
    GREEN = "GREEN"
    YELLOW = "YELLOW"
    BLACK = "BLACK"

class Iphone:
    def set_model(self, model):
        self.model = model
        return self

    def set_color(self, color: IphoneColor):
        self.color = color
        return self

    def set_memory(self, memory):
        self.memory = memory
        return self

    def set_price(self, price):
        self.price = price
        return self

    def set_processor(self, processor):
        self.processor = processor
        return self
    
    def set_number_of_cameras(self, number_of_cameras):
        self.number_of_cameras = number_of_cameras
        return self

    def get_info(self):
        return f"Model: {self.model}, Color: {self.color}, Memory: {self.memory}, Price: {self.price}, Processor: {self.processor}, Number of Cameras: {self.number_of_cameras}"
    
    
class IphoneBuilder(ABC):
    def __init__(self) -> None:
        self.iphone = Iphone()
        
    @abstractmethod
    def set_model(self):
        pass
    
    @abstractmethod
    def set_color(self):
        pass
    
    @abstractmethod
    def set_memory(self):
        pass
    
    @abstractmethod
    def set_price(self):
        pass
    
    @abstractmethod
    def set_processor(self):
        pass
    
    @abstractmethod
    def set_number_of_cameras(self):
        pass
    
    
class Iphone15Builder(IphoneBuilder):
    def set_model(self):
        self.iphone.set_model("Iphone 15")
        return self
    
    def set_color(self, color: IphoneColor = IphoneColor.BLACK):
        self.iphone.set_color(color)
        return self
    
    def set_memory(self):
        self.iphone.set_memory("128 GB")
        return self
    
    def set_price(self):
        self.iphone.set_price("799$")
        return self
    
    def set_processor(self):
        self.iphone.set_processor("A16 Bionic")
        return self
    
    def set_number_of_cameras(self):
        self.iphone.set_number_of_cameras("2")
        return self
    
class Iphone15PlusBuilder(IphoneBuilder):
    def set_model(self):
        self.iphone.set_model("Iphone 15 Plus")
        return self
    
    def set_color(self, color: IphoneColor = IphoneColor.BLACK):
        self.iphone.set_color(color)
        return self
    
    def set_memory(self):
        self.iphone.set_memory("256 GB")
        return self
    
    def set_price(self):
        self.iphone.set_price("999$")
        return self
    
    def set_processor(self):
        self.iphone.set_processor("A16 Bionic")
        return self
    
    def set_number_of_cameras(self):
        self.iphone.set_number_of_cameras("2")
        return self
    
class Iphone15ProBuilder(IphoneBuilder):
    def set_model(self):
        self.iphone.set_model("Iphone 15 Pro")
        return self
    
    def set_color(self, color: IphoneColor = IphoneColor.BLACK):
        self.iphone.set_color(color)
        return self
    
    def set_memory(self):
        self.iphone.set_memory("512 GB")
        return self
    
    def set_price(self):
        self.iphone.set_price("1199$")
        return self
    
    def set_processor(self):
        self.iphone.set_processor("A16 Bionic")
        return self
    
    def set_number_of_cameras(self):
        self.iphone.set_number_of_cameras("3")
        return self


class AppleStore:
    def __init__(self, builder: IphoneBuilder) -> None:
        self.builder = builder
        
    def build_iphone(self):
        # Command Chaining, as all the methods return self.
        return self.builder.set_model().set_color().set_memory().set_price().set_processor().set_number_of_cameras().iphone

if __name__ == "__main__":
    iphone15 = AppleStore(Iphone15Builder()).build_iphone()
    iphone15_plus = AppleStore(Iphone15PlusBuilder()).build_iphone()
    iphone15_pro = AppleStore(Iphone15ProBuilder()).build_iphone()
    
    print(iphone15.get_info())
    print(iphone15_plus.get_info())
    print(iphone15_pro.get_info())