import json


def test_reg_positive(reg, config):
    reg.regAccount_step1(config["web"]["reg_email"])
    assert 'YOUR PERSONAL INFORMATION' in reg.create_acc.account_creation_form.text
    assert reg.create_acc.emailCreate_input.get_attribute("value") == config["web"]["reg_email"]
    reg.regAccount_step2(gender='F', firstname='Natali', lastname='Tiutiunnyk', password=config["web"]["password"], bithday='3', monBithDay='10', yearBithDay='1995',
                         newsLetter='Yes', receiveOffer='Yes')
    assert reg.create_acc.firstnameAdd_input.get_attribute("value") ==  reg.create_acc.firstname_input.get_attribute("value")
    assert reg.create_acc.lastnameAdd_input.get_attribute("value") == reg.create_acc.lastname_input.get_attribute("value")
    reg.regAccount_step3(companyAdd='Luxoft', add1='Address1', add2='Address1', cityAdd='Kyiv', state='5',
                     postcode='00000', country='21', additionInfo='test1', homePhoneAdd='2125484', mobilePhoneAdd='658542', aliasAdd='54854545')