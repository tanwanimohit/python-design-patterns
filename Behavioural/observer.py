from abc import ABC, abstractmethod
from typing import List
import time

# Observer / Subscriber
class Customer(ABC):
    
    @abstractmethod
    def update(self, stock_quantity):
        raise NotImplementedError
    
# Subject / Publisher
class Store(ABC):

    @abstractmethod
    def register_observer(self, observer):
        raise NotImplementedError
    
    @abstractmethod
    def register_observer(self, observer):
        raise NotImplementedError
    
    @abstractmethod
    def register_observer(self, observer):
        raise NotImplementedError

class BookCustomer(Customer):
    
    def __init__(self, store: Store):
        self._store = store
        self._store.register_observer(self)
    
    def update(self, stock_quantity):
        if stock_quantity > 0:
            print(f"Hello there! Book is back in stock! Quantiles: {stock_quantity}")


class BookStore(Store):
    _observers: List[Customer] = []
    _quantity = 0
    
    def register_observer(self, observer: Customer):
        self._observers.append(observer)
        
    def unregister_observer(self, observer: Customer):
        self._observers.remove(observer)
        
    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._quantity)
            
    def set_quantity(self, number):
        self._quantity = number
        print("Book Quantity Updated! Notifying observers... ")
        self.notify_observers()

def run():
    book_store = BookStore()
    _ = BookCustomer(book_store)
    customer2 = BookCustomer(book_store)
    
    book_store.set_quantity(0)
    time.sleep(2)
    
    book_store.set_quantity(100)
    time.sleep(2)
    book_store.unregister_observer(customer2)
    time.sleep(2)
    book_store.set_quantity(10) 

if __name__ == "__main__":
    run()