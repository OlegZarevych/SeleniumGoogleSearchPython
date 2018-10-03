import unittest
from Browser import Browser as browser

class BaseTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = browser.getBrowser("firefox")
        self.driver.open("http://google.com")
        
    def tearDown(self):
        self.driver.close()
        