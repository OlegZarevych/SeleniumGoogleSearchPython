from BrowserFactory.FirefoxBrowser import FirefoxBrowser

class Browser():
            
                
    def getBrowser(self):  
        browsers = {
            "firefox": FirefoxBrowser() 
            }
        return browsers.get(self.browserName, lambda: 'Invalid browser name')
    
    def __init__(self, browserName):
        self.browserName = browserName
        
    