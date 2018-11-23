from Tests.BaseTest import BaseTest
from Pages.GoogleMainPage import GoogleMainPage
import logging

class TestGoogleMain(BaseTest):
    
    def test_google_page(self):
        logging.info("Test is started:", self._testMethodName)
        text = "Python"
        main_page = GoogleMainPage(self.driver)
        result_page = main_page.search_text(text)
        first_link = result_page.get_first_link()
        self.assertTrue(text in first_link.text, "No searched text in first link")