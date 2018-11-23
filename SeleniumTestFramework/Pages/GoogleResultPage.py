from selenium.webdriver.common.by import By
from Pages.Page import Page

class GoogleResultPage(Page):

    FIRST_LINK = "//div[@class='bkWMgd'][1]//a/h3"
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def check_resut_exist(self, result):
        pass
    
    def get_first_link(self):
        return self.find_element(self.FIRST_LINK)