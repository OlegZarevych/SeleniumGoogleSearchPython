from selenium import webdriver

class Browser():
    
    driver = None
    
    def __init__(self, browserName):
        self.browserName = browserName
          
    def getBrowser(self):  
        browsers = {
            "firefox": self.__run_firefox_browser() 
            }
        return browsers.get(self.browserName, lambda: 'Invalid browser name')
        
    def open(self, url):
        self.driver.get(url)
        
    def close(self):
        self.driver.quit();
        
    def __run_firefox_browser(self):
        self.driver = webdriver.Firefox(executable_path="/usr/bin/geckodriver")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        return self.driver