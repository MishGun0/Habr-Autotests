from page import *


def test_basic_search(driver):
    click_search_form(driver)

    type_text(driver, 'Selenium')

    click_search_button(driver)

    count_articles_number(driver)

    count_pages_number(driver)

