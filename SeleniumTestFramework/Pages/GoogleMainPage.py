from selenium.webdriver.common.by import By
from Pages.GoogleResultPage import GoogleResultPage
from Pages.Page import Page

class GoogleMainPage(Page):
    
    SEARCH_INPUT = (By.NAME, 'q')
    SEARCH_BTN = (By.NAME, 'btnK')
       
    def __init__(self, driver):
        super().__init__(driver)
        pass
    
    def search_text(self, text):
        self.find_element(self.SEARCH_INPUT)
        self.find_element(self.SEARCH_BTN)
        return GoogleResultPage