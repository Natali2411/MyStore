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
        return self.driver.find_element_by_id('email')

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

    @property
    def address2Add_input(self):
        return self.driver.find_element_by_id('address2')

    @property
    def cityAdd_input(self):
        return self.driver.find_element_by_id('city')

    @property
    def stateAdd_select(self):
        return self.driver.find_element_by_id('id_state')

    @property
    def postcodeAdd_select(self):
        return self.driver.find_element_by_id('postcode')

    @property
    def countryAdd_select(self):
        return self.driver.find_element_by_id('id_country')

    @property
    def additionInfoAdd_input(self):
        return self.driver.find_element_by_id('other')

    @property
    def homePhoneAdd_input(self):
        return self.driver.find_element_by_id('phone')

    @property
    def mobilePhoneAdd_input(self):
        return self.driver.find_element_by_id('phone_mobile')

    @property
    def aliasAdd_input(self):
        return self.driver.find_element_by_id('alias')

    @property
    def submitAccount_input(self):
        return self.driver.find_element_by_id('submitAccount')
