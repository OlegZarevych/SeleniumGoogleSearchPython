from abc import ABC, abstractmethod

class AbstractBrowserFactory(object, ABC):
    
    @abstractmethod
    def open(self, url):
        pass
    
    @abstractmethod    
    def close(self):
        pass
        
    