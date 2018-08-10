import unittest
import Browser

class BaseTest(unittest.TestCase):
    
    self.driver
    
    def setUp(self):
        self.driver = Browser.getBrowser("firefox")
        self.driver.open("http://google.com")
        
    def tearDown(self):
        self.driver.close()
        