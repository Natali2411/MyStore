from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.start_page import StartPage
from pages.authentication_page import AuthenticationPage
from pages.create_acc_page import CreateAccount
from selenium.webdriver.support.ui import Select
from pages.myaccount_page import MyAccount


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
        self.myAcc = MyAccount(driver, base_url)

    def quit(self):
        self.wd.quit()

    def regAccount_step1(self, email):
        self.start_page.signIn_link.click()
        self.authent_page.emailCreate_input.clear()
        self.authent_page.emailCreate_input.send_keys(email)
        self.authent_page.submitCreate_but.click()

    def regAccount_step2(self, gender=None, firstname=None, lastname=None, password=None, bithday=None, monBithDay=None, yearBithDay=None,
                         newsLetter=None, receiveOffer=None):
        if gender == 'F':
            self.create_acc.female_radio_but.click()
        elif gender == 'M':
            self.create_acc.male_radio_but.click()
        self.create_acc.firstname_input.clear()
        self.create_acc.firstname_input.send_keys(firstname)
        self.create_acc.lastname_input.clear()
        self.create_acc.lastname_input.send_keys(lastname)
        self.create_acc.passwd_input.clear()
        self.create_acc.passwd_input.send_keys(password)
        day = Select(self.create_acc.birthDay_select)
        day.select_by_value(bithday)
        month = Select(self.create_acc.birthMon_select)
        month.select_by_value(monBithDay)
        year = Select(self.create_acc.birthYear_select)
        year.select_by_value(yearBithDay)
        if newsLetter == 'Yes':
            self.create_acc.newsletter_check.click()
        else:
            pass
        if receiveOffer == 'Yes':
            self.create_acc.recieveOffer_check.click()
        else:
            pass

    def regAccount_step3(self, companyAdd=None, add1=None, add2=None, cityAdd=None, state=None, postcode=None, country=None,
                         additionInfo=None, homePhoneAdd=None, mobilePhoneAdd=None, aliasAdd=None):
        self.create_acc.companyAdd_input.clear()
        self.create_acc.companyAdd_input.send_keys(companyAdd)
        self.create_acc.address1Add_input.clear()
        self.create_acc.address1Add_input.send_keys(add1)
        self.create_acc.address2Add_input.clear()
        self.create_acc.address2Add_input.send_keys(add2)
        self.create_acc.cityAdd_input.clear()
        self.create_acc.cityAdd_input.send_keys(cityAdd)
        stateAdd = Select(self.create_acc.stateAdd_select)
        stateAdd.select_by_value(state)
        self.create_acc.postcodeAdd_input.clear()
        self.create_acc.postcodeAdd_input.send_keys(postcode)
        countryAdd = Select(self.create_acc.countryAdd_select)
        countryAdd.select_by_value(country)
        self.create_acc.additionInfoAdd_input.clear()
        self.create_acc.additionInfoAdd_input.send_keys(additionInfo)
        self.create_acc.homePhoneAdd_input.clear()
        self.create_acc.homePhoneAdd_input.send_keys(homePhoneAdd)
        self.create_acc.mobilePhoneAdd_input.clear()
        self.create_acc.mobilePhoneAdd_input.send_keys(mobilePhoneAdd)
        self.create_acc.aliasAdd_input.clear()
        self.create_acc.aliasAdd_input.send_keys(aliasAdd)
        self.create_acc.register_but.click()