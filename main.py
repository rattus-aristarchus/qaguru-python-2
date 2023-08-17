import pytest
from selene.support.shared import browser
from selene import be, have
from selenium import webdriver


@pytest.fixture(scope="function", autouse=True)
def setup_browser():
    browser.config.driver = webdriver.Chrome()
    browser.config.window_height = 600
    browser.config.window_height = 1200

    yield

    browser.close()


def test_search_positive():
    # act
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    # assert
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_search_negative():
    # act
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('asd;lkadklsdk;laskl;dsa;kldasklsda').press_enter()
    # assert
    browser.element('[class="card-section"]').should(have.text('ничего не найдено'))

