import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def open_chrome_page(chrome_driver):
    browser.config.driver = chrome_driver
    browser.open('https://google.com')


def test_search_positive(open_chrome_page):
    # act
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    # assert
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_search_negative(open_chrome_page):
    # act
    browser.element('[name="q"]').should(be.blank).type('asd;lkadklsdk;laskl;dsa;kldasklsda').press_enter()
    # assert
    browser.element('[id="topstuff"]').should(have.text('ничего не найдено'))

