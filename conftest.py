import time

import pytest
from selenium.webdriver.chrome import webdriver


def setup():
    print('set up')
    driver = webdriver.WebDriver('chromedriver')

    driver.get('https://habr.com/ru/all/')

    time.sleep(1)

    return driver


def tear_down(driver):
    print('tear down')
    driver.quit()


@pytest.fixture
def driver():
    return setup()
