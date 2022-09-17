from page import *

def test_empty_search(driver):

    click_search_form(driver)

    type_text(driver, 'sdsfhthrth')

    click_search_button(driver)

    count_articles_number(driver)

    check_empty_page_text(driver)

