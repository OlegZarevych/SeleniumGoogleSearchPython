from BrowserFactory.Browser import Browser


class Page(object):
    
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
                
    def find_element(self, locator):
        element = self.driver.find_element_by_xpath(locator)
        return element
                