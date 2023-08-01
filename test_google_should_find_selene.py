from selene.support.shared import browser
from selene import be, have
from selenium import webdriver

# без этого блока браузер запускается пустым и ничего не происходит
options = webdriver.ChromeOptions()
options.add_argument('--remote-debugging-port=9222')
browser.config.driver_options = options

# собственно задание
browser.open('https://google.com')
browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))
