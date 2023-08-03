
import pytest
from selene.support.shared import browser
from selenium import webdriver


@pytest.fixture(scope="module")
def chrome_options():
    options = webdriver.ChromeOptions()

    """
    Без этого браузер запускается пустым. Почему - так и не понял(( Решение отсюда:
    https://stackoverflow.com/questions/50642308/webdriverexception-unknown-error-devtoolsactiveport-file-doesnt-exist-while-t/66194969#66194969
    """
    options.add_argument('--remote-debugging-port=9222')

    return options


@pytest.fixture(scope="module")
def assemble_chrome(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(800, 600)
    browser.config.driver = driver
