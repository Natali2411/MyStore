from selenium import webdriver
import pytest
import json
import os
from models.mystore_app import MyStore
import random
import string


@pytest.fixture(scope="session")
def config():
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
    with open(filename)as f:
        return json.load(f)

@pytest.fixture()
def reg(config):
    driver = webdriver.Chrome()
    app = MyStore(driver=driver, base_url=config["web"]["base_url"])
    yield app
    #app.quit()

@pytest.fixture()
def ran_email(size1=5, size2=3, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size1))+'@'+''.join(random.choice(chars) for _ in range(size2))+'.'+''.join(random.choice(chars) for _ in range(size2))