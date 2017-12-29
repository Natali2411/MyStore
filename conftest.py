from selenium import webdriver
import pytest
import json
import os
from models.mystore_app import MyStore

@pytest.fixture(scope="session")
def config():
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
    with open(filename)as f:
        return json.load(f)

@pytest.fixture()
def reg(config):
    driver = webdriver.Firefox()
    app = MyStore(driver=driver, base_url=config["web"]["base_url"])
    yield app