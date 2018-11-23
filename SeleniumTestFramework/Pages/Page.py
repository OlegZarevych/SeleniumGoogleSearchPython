from BrowserFactory.Browser import Browser


class Page(object):
    
    
    def __init__(self, driver):
        self.driver = driver
                
    def find_element(self, locator):
        return self.driver.find_element_by_xpath(locator)
                