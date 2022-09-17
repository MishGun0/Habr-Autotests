import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


def setup():
    print('set up')
    driver = webdriver.WebDriver('chromedriver')

    driver.get('https://habr.com/ru/all/')

    time.sleep(3)

    return driver


def tear_down(driver):
    print('tear down')
    driver.quit()


def count_pages_number(driver):
    # посчитать количество страниц (50)
    last_page_locator = By.XPATH, '(//*[@class="tm-pagination__page"])[last()]'
    last_page_number = driver.find_element(*last_page_locator)
    element_text = last_page_number.text
    print(f'Number of pages is {element_text}')
    time.sleep(1)


def count_articles_number(driver):
    # посчитать количество записей (20)
    article_locator = By.TAG_NAME, 'article'
    articles = driver.find_elements(*article_locator)
    print(f'Number of articles is{len(articles)})')
    time.sleep(1)


def click_search_button(driver):
    # нажать на иконку поиска
    search_icon_locator = By.CSS_SELECTOR, 'span.tm-search__icon'
    search_icon = driver.find_element(*search_icon_locator)
    search_icon.click()
    time.sleep(2)


def type_text(driver, text):
    # вбить текст
    search_input_locator = By.CLASS_NAME, 'tm-input-text-decorated__input'
    search_input = driver.find_element(*search_input_locator)
    text_to_search = text
    search_input.send_keys(text_to_search)


def click_search_form(driver):
    # Открыть поиск
    search_button_locator = By.CSS_SELECTOR, 'a.tm-header-user-menu__item'
    search_button = driver.find_element(*search_button_locator)
    search_button.click()
    time.sleep(2)


def test_basic_search(driver):
    click_search_form(driver)

    type_text(driver, 'Selenium')

    click_search_button(driver)

    count_articles_number(driver)

    count_pages_number(driver)


if __name__ == '__main__':
    driver_object = setup()

    try:
        test_basic_search(driver_object)
    except NoSuchElementException as error:
        print(f'Test failed, reason: {error}')

    tear_down(driver_object)
