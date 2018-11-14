from abc import ABC, abstractmethod

# This class is obsolete

class AbstractFactory(ABC):
    
    @abstractmethod
    def open(self, url):
        pass
    
    @abstractmethod    
    def close(self):
        pass
        
    