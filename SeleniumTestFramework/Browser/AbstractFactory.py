from abc import ABC, abstractmethod

class AbstractFactory(object, ABC):
    
    @abstractmethod
    def open(self, url):
        pass
    
    @abstractmethod    
    def close(self):
        pass
        
    