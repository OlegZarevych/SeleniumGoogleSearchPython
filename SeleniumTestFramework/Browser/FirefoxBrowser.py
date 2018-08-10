
from selenium import webdriver
from lib2to3.pgen2 import driver

class FirefoxBrowser(AbstractBrowserFactory):
    
    self.driver
    
    def __init__(self):
        driver = webdriver.Firefox
        driver.fullscreen_window()
    
    def open(self, url):
        driver.open(url)
        
    def close(self):
        driver.close();
        