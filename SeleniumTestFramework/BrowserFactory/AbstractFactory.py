from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    
    @abstractmethod
    def open(self, url):
        pass
    
    @abstractmethod    
    def close(self):
        pass
        
    