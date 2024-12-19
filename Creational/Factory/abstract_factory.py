"""
When to Use Which Pattern?

Simple Factory: Use it when you have a limited number of classes to instantiate 
and you want to centralize the creation logic. It is a simpler 
and less flexible pattern compared to the Abstract Factory.


Abstract Factory: Use it when you need to create families of related or dependent objects. 
It provides a more flexible and extensible solution, adhering to the Open/Closed Principle.

In summary, the Simple Factory is suitable for simpler scenarios with fewer types of objects, 
while the Abstract Factory is better for more complex scenarios involving multiple families of related objects.
"""

from abc import ABC, abstractmethod

class Burger(ABC):
    @abstractmethod
    def create_burger(self):
        pass
    
class Drink(ABC):
    @abstractmethod
    def create_drink(self):
        pass

class CheeseBurger(Burger):
    
    def create_burger(self):
        print("Creating Cheese Burger")

class PannerBurger(Burger):
    
    def create_burger(self):
        print("Creating Panner Burger")
        
class Pepsi(Drink):
    
    def create_drink(self):
        print("Pepsi Creating..")
        
class Coke(Drink):
    
    def create_drink(self):
        print("Coke Creating..")

# Burger's Abstract Factory Class.
class BurgerStore():
    
    @abstractmethod
    def create_burger(self):
        raise NotImplementedError
    
    @abstractmethod
    def create_drink(self):
        raise NotImplementedError
    
    @staticmethod
    def create_store(type):
        if type.lower() == "mcd":
            return McdStore()
        elif type.lower() == "bk":
            return BkStore()
        else:
            raise NotImplementedError        

class McdStore(BurgerStore):
    
    def get_burger(self):
        return PannerBurger()
        
    def get_drink(self):
        return Coke()
    
class BkStore(BurgerStore):
    
    def get_burger(self):
        return CheeseBurger()
        
    def get_drink(self):
        return Pepsi()
        
        

def restaurant():
   store = input("Which Store?")
   store = BurgerStore.create_store(store)
   burger = store.get_burger()
   drink = store.get_drink()
   burger.create_burger()
   drink.create_drink()
    
    

if __name__ == "__main__":
    restaurant()