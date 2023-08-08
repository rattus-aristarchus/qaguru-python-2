
import pytest
from selene.support.shared import browser
from selenium import webdriver


@pytest.fixture()
def chrome_driver():
    driver = webdriver.Chrome()
    return driver
