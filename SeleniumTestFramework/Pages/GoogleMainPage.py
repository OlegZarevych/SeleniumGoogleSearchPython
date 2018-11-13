from selenium.webdriver.common.by import By
from Pages.GoogleResultPage import GoogleResultPage
from Pages.Page import Page

class GoogleMainPage(Page):
   
    def __init__(self):
        pass
    
    SEARCH_INPUT = (By.NAME, 'q')
    SEARCH_BTN = (By.NAME, 'btnK')
    
    def search_text(self, text):
        self.SEARCH_INPUT.send_keys(text)
        self.SEARCH_BTN.submit()
        return GoogleResultPage