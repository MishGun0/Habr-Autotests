from page import *


def test_main_page(driver):
    page = MainPage(driver)
    page.open()

    count_articles_number(driver)
    count_pages_number(driver)

