from test_1 import *


def test_empty_search(driver):
    click_search_form(driver)

    type_text(driver, 'sdsfhthrth')

    click_search_button(driver)

    count_articles_number(driver)

    check_empty_page_text(driver)


def check_empty_page_text(driver):
    empty_res_locator = By.CLASS_NAME, 'tm-empty-placeholder__text'
    empty_results = driver.find_element(*empty_res_locator)
    print(f'Text on page: {empty_results.text}')


if __name__ == '__main__':
    driver_object = setup()

    try:
        test_empty_search(driver_object)
    except NoSuchElementException as error:
        print('Test failed, {error}')

    tear_down(driver_object)
