from pages.create_acc_page import CreateAccount

class MyAccount(CreateAccount):
    @property
    def main_block(self):
        return self.driver.find_element_by_id('center_column')