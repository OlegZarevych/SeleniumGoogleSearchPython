import Browser.FirefoxBrowser

class Browser():
    
    def getBrowser(self, browserName):
        
        browsers = {
            "firefox": Browser.FirefoxBrowser 
            }
        return browsers.get(browserName, lambda: 'Invalid browser name')