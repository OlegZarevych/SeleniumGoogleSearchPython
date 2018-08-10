import FirefoxBrowser

class Browser():
    
    def getBrowser(self, browserName):
        
        browsers = {
            "firefox": FirefoxBrowser 
            }
    
    return browsers.get(browserName, lambda: 'Invalid browser name')