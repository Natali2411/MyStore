import json


def test_registration(reg, config):
    reg.regAccount_step1(config["web"]["reg_email"])
    assert 'YOUR PERSONAL INFORMATION' in reg.create_acc.account_creation_form.text
