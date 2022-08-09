import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.WebDriver("chromedriver")

driver.get("https://habr.com/ru/all/")

time.sleep(3)

search_button_locator = '[class="tm-svg-img tm-header-user-menu__icon tm-header-user-menu__icon_search"]'
search_button = driver.find_element(By.CSS_SELECTOR, search_button_locator)
search_button.click()

time.sleep(3)

# вбить текст
search_input_locator = By.CLASS_NAME, "tm-input-text-decorated__input"
search_input = driver.find_element(*search_input_locator)
text_to_search = "Selenium"
search_input.send_keys(text_to_search)

# нажать на иконку поиска
search_icon_locator = By.CSS_SELECTOR, 'span.tm-search__icon'
search_icon = driver.find_element(*search_icon_locator)
search_icon.click()

time.sleep(3)
# посчитать количество записей (20)
article_locator = By.TAG_NAME, "article"
articles = driver.find_elements(*article_locator)
print(f"Number of articles is{len(articles)})")

time.sleep(3)

# посчитать количество страниц (50)
last_page_locator = By.XPATH, '(//*[@class="tm-pagination__page"])[last()]'
last_page_number = driver.find_element(*last_page_locator)
element_text = last_page_number.text
print(f'Number of pages is {element_text}')

driver.quit()