import time

from selenium.webdriver.common.by import By


def test_empty_search(driver):
    # открыть поиск
    search_button_locator = By.CSS_SELECTOR, 'a.tm-header-user-menu__item'
    search_button = driver.find_element(*search_button_locator)
    search_button.click()
    time.sleep(2)

    # вбить текст
    search_input_locator = By.CLASS_NAME, 'tm-input-text-decorated__input'
    search_input = driver.find_element(*search_input_locator)
    text_to_search = 'sdsfhthrth'
    search_input.send_keys(text_to_search)
    time.sleep(1)

    # нажать на иконку поиска
    search_icon_locator = By.CSS_SELECTOR, 'span.tm-search__icon'
    search_icon = driver.find_element(*search_icon_locator)
    search_icon.click()
    time.sleep(2)

    # посчитать количество записей (0)
    article_locator = By.TAG_NAME, 'article'
    articles = driver.find_elements(*article_locator)
    print(f'Number of articles is{len(articles)}')
    time.sleep(1)

    # проверяем текст
    empty_res_locator = By.CLASS_NAME, 'tm-empty-placeholder__text'
    empty_results = driver.find_element(*empty_res_locator)
    print(f'Text on page: {empty_results.text}')
