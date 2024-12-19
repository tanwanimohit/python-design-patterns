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


def restaurant():
    burger = input("Which Burger? ")
    burger_obj = None
    if burger == "cheese":
        burger_obj = CheeseBurger()
    elif burger == "paneer":
        burger_obj = PannerBurger()
    else:
        print("Invaild Input")
    burger_obj.create_burger()
    
    """
    Problem: If we need to introduce new burger then client have to modify this code.
    this makes the client tightly coupled. 
    Solution: Create factory which will take care of creation and we dont need to expose logic
    to client. this makes code loosely coupled.
    """

if __name__ == "__main__":
    restaurant()