from page import *

def test_main_page(driver):
    page = MainPage(driver)
    page.open()

    print(page.count_articles_number())
    print(page.count_pages_number())
