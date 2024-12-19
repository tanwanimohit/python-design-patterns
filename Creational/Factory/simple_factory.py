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
    
class CheeseBurger(Burger):
    
    def create_burger(self):
        print("Creating Cheese Burger")

class PannerBurger(Burger):
    
    def create_burger(self):
        print("Creating Panner Burger")

# Burger's Factory Class.
class BurgerStore():
    @staticmethod
    def get_burger(burger):
        burger_obj = None
        if burger.lower() == "cheese":
            burger_obj = CheeseBurger()
        elif burger.lower() == "panner":
            burger_obj = PannerBurger()
        else:
            print("Invalid Input")
        return burger_obj
        

def restaurant():
    burger = input("Which Burger? ")
    burger_obj: Burger = BurgerStore.get_burger(burger)
    burger_obj.create_burger() 
    
    

if __name__ == "__main__":
    restaurant()