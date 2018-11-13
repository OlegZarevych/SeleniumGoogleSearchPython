from selenium import webdriver
from BrowserFactory.AbstractFactory import AbstractFactory

class FirefoxBrowser(AbstractFactory):
    
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path="/usr/bin/geckodriver")
        self.driver.maximize_window()
    
    def open(self, url):
        self.driver.get(url)
        
    def close(self):
        self.driver.quit();
        