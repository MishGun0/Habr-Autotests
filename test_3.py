from page import *


def test_main_page(driver):
    count_articles_number(driver)
    count_pages_number(driver)


if __name__ == '__main__':
    driver_object = setup()

    try:
        test_main_page(driver_object)
    except NoSuchElementException as error:
        print(f'Test failed, {error}')

    tear_down(driver_object)
