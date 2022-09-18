from page import *


def test_basic_search(driver):
    page = MainPage(driver)
    page.open()

    page = page.click_search()

    page.search('Selenium')

    print(page.count_articles_number())
    print(page.count_pages_number())
