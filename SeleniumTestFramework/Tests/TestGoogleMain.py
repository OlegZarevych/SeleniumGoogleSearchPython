from Tests.BaseTest import BaseTest
from Pages.GoogleMainPage import GoogleMainPage
import logging

class TestGoogleMain(BaseTest):
    
    def test_google_page(self):
        logging.info("Test is started:", self._testMethodName)
        main_page = GoogleMainPage(self.driver)
        main_page.search_text("qa")