import time
from locators import *
from selenium.common.exceptions import NoSuchElementException

class MainPage:
    url = 'https://habr.com/ru/all/'

    def __init__(self, webdriver):
        self.__webdriver = webdriver

    def open(self):
        self.__webdriver.get(self.url)

    @property
    def search_button(self):
        return self.__webdriver.find_element(*search_button_locator)

    def click_search(self):
        time.sleep(2)

        self.search_button.click()

        time.sleep(2)

        return SearchResultsPage(self.__webdriver)

class SearchResultsPage:
    url = 'https://habr.com/ru/search'

    def __init__(self, webdriver):
        self.__webdriver = webdriver
    @property
    def search_input(self):
        return self.__webdriver.find_element(*search_input_locator)
    @property
    def search_button(self):
        return self.__webdriver.find_element(*search_icon_locator)

    def search(self, search_text):
        self.search_input.send_keys(search_text)
        self.search_button.click()

        time.sleep(2)

    @property
    def last_page_number(self):
        return self.__webdriver.find_element(*last_page_locator)

    def count_pages_number(self):
        return self.last_page_number.text

    def go_to_last_page(self):
        self.last_page_number.click()

    @property
    def articles(self):
        return self.__webdriver.find_elements(*article_locator)

    def count_articles_number(self):
        return len(self.articles)

    @property
    def empty_result_banner(self):
        return self.__webdriver.find_element(*empty_res_locator)

    def get_empty_page_text(self):
        return self.empty_result_banner.text
