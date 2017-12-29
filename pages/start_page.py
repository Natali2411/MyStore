from selenium.webdriver.common.by import By
from pages.page import Page

class StartPage(Page):
    @property
    def signIn_link(self):
        return self.driver.find_element_by_css_selector('.login')
