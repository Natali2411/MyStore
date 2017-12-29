from pages.start_page import StartPage


class AuthenticationPage(StartPage):
    @property
    def createAccount_form(self):
        return self.driver.find_element_by_id('create-account_form')

    @property
    def emailCreate_input(self):
        return self.driver.find_element_by_id('email_create')

    @property
    def submitCreate_but(self):
        return self.driver.find_element_by_id('SubmitCreate')