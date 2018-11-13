from Tests.BaseTest import BaseTest
from Pages.GoogleMainPage import GoogleMainPage

class TestGoogleMain(BaseTest):
    
    def test_google_page(self):
        main_page = GoogleMainPage()
        main_page.search_text("qa")
        