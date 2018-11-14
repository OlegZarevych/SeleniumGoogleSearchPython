import unittest
from BrowserFactory.Browser import Browser

class BaseTest(unittest.TestCase):
    
    url = "http://google.com"
    driver = None
    
    def setUp(self):
        browser = Browser("firefox")
        self.driver = browser.getBrowser()
        browser.open(self.url)
        
    def tearDown(self):
        self.driver.close()
        
        
if __name__ == "__main__":
    unittest.main()