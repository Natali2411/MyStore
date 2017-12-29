from pages.authentication_page import AuthenticationPage


class CreateAccount(AuthenticationPage):
    @property
    def account_creation_form(self):
        return self.driver.find_element_by_id('account-creation_form')
# Personal information block
    @property
    def female_radio_but(self):
        return self.driver.find_element_by_id('id_gender2')

    @property
    def male_radio_but(self):
        return self.driver.find_element_by_id('id_gender1')

    @property
    def firstname_input(self):
        return self.driver.find_element_by_id('customer_firstname')

    @property
    def lastname_input(self):
        return self.driver.find_element_by_id('customer_lastname')

    @property
    def emailCreate_input(self):
        pass

    @property
    def passwd_input(self):
        return self.driver.find_element_by_id('passwd')

    @property
    def birthDay_select(self):
        return self.driver.find_element_by_id('days')

    @property
    def birthMon_select(self):
        return self.driver.find_element_by_id('months')

    @property
    def birthYear_select(self):
        return self.driver.find_element_by_id('years')

    @property
    def newsletter_check(self):
        return self.driver.find_element_by_id('newsletter')

    @property
    def recieveOffer_check(self):
        return self.driver.find_element_by_id('option')
# Address block
    @property
    def firstnameAdd_input(self):
        return self.driver.find_element_by_id('firstname')

    @property
    def lastnameAdd_input(self):
        return self.driver.find_element_by_id('lastname')

    @property
    def companyAdd_input(self):
        return self.driver.find_element_by_id('company')

    @property
    def address1Add_input(self):
        return self.driver.find_element_by_id('address1')