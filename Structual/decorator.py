from abc import ABC, abstractmethod
class IBurger(ABC):

    @abstractmethod
    def cost(self):
        pass    
     
    @abstractmethod
    def description(self):
        pass

class WheatBurger(IBurger):

    def cost(self):
        return 120.0
    
    def description(self):
        return "Whole Wheat Burger"
    
class RegularBurger(IBurger):

    def cost(self):
        return 100.0
    
    def description(self):
        return "Regular Burger"
    
class BurgerDecorator(IBurger):
    
    def __init__(self, burger):
        self.burger:IBurger = burger
        
class CheeseDecorator(BurgerDecorator):
    
    def __init__(self, burger):
        super().__init__(burger)
        
    def cost(self):
        return 20.0 + self.burger.cost()
    
    def description(self):
        return self.burger.description() + ", Cheese"
    

class VegetableDecorator(BurgerDecorator):
    
    def __init__(self, burger):
        super().__init__(burger)
        
    def cost(self):
        return 20.0 + self.burger.cost()
    
    def description(self):
        return self.burger.description() + ", Vegetables"
    
if __name__ == "__main__":
    my_burger = VegetableDecorator(CheeseDecorator(WheatBurger()))
    print(my_burger.cost())
    print(my_burger.description())