from selenium import webdriver
from Browser.AbstractFactory import AbstractFactory

class FirefoxBrowser(AbstractFactory):
    
    def __init__(self):
        self.driver = webdriver.Firefox
        self.driver.fullscreen_window()
    
    def open(self, url):
        self.driver.open(url)
        
    def close(self):
        self.driver.close();
        