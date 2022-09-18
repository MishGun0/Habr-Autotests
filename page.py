import time
from locators import *
from selenium.common.exceptions import NoSuchElementException

class HabrBase:
    def __init__(self, webdriver):
        self.webdriver = webdriver

    @property
    def last_page_number(self):
        return self.webdriver.find_element(*last_page_locator)

    def count_pages_number(self):
        return self.last_page_number.text

    def go_to_last_page(self):
        self.last_page_number.click()

    @property
    def articles(self):
        return self.webdriver.find_elements(*article_locator)

    def count_articles_number(self):
        return len(self.articles)

class MainPage(HabrBase):
    url = 'https://habr.com/ru/all/'

    def open(self):
        self.webdriver.get(self.url)

    @property
    def search_button(self):
        return self.webdriver.find_element(*search_button_locator)

    def click_search(self):
        time.sleep(2)

        self.search_button.click()

        time.sleep(2)

        return SearchResultsPage(self.webdriver)

class SearchResultsPage(HabrBase):
    url = 'https://habr.com/ru/search'

    @property
    def search_input(self):
        return self.webdriver.find_element(*search_input_locator)
    @property
    def search_button(self):
        return self.webdriver.find_element(*search_icon_locator)

    def search(self, search_text):
        self.search_input.send_keys(search_text)
        self.search_button.click()

        time.sleep(2)

    @property
    def empty_result_banner(self):
        return self.webdriver.find_element(*empty_res_locator)

    def get_empty_page_text(self):
        return self.empty_result_banner.text
