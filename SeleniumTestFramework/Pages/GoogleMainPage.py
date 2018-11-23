from selenium.webdriver.common.by import By
from Pages.GoogleResultPage import GoogleResultPage
from Pages.Page import Page

class GoogleMainPage(Page):
    
    #SEARCH_INPUT = (By.NAME, 'q')
    SEARCH_INPUT = "//input[@name='q']"
    SEARCH_BTN = "//input[@name='btnK']"
       
    def __init__(self, driver):
        super().__init__(driver)
        pass
    
    def search_text(self, text):
        self.find_element(self.SEARCH_INPUT).send_keys(text)
        self.find_element(self.SEARCH_BTN).submit()
        return GoogleResultPage