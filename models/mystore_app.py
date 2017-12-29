from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.start_page import StartPage
from pages.authentication_page import AuthenticationPage
from pages.create_acc_page import CreateAccount

class MyStore():
    def __init__(self, driver, base_url):
        self.wd = driver
        self.wd.implicitly_wait(5)
        self.wd.get(base_url)
        self.wait = WebDriverWait(driver, 5)
        self.wd.maximize_window()
        self.start_page = StartPage(driver, base_url)
        self.authent_page = AuthenticationPage(driver, base_url)
        self.create_acc = CreateAccount(driver, base_url)

    def regAccount_step1(self, email):
        self.start_page.signIn_link.click()
        self.authent_page.emailCreate_input.clear()
        self.authent_page.emailCreate_input.send_keys(email)
        self.authent_page.submitCreate_but.click()

    def regAccount_step2(self, gender=None, firstname=None, lastname=None, ):
        if gender == 'F':
            self.create_acc.female_radio_but.click()
        elif gender == 'M':
            self.create_acc.male_radio_but.click()
        self.create_acc.firstname_input.clear()
        self.create_acc.firstname_input.send_keys(firstname)
        self.create_acc.lastname_input.clear()
        self.create_acc.lastname_input.send_keys(firstname)
