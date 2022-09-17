from page import *


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

