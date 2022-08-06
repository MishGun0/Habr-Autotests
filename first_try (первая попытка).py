import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.WebDriver("chromedriver")

driver.get("https://habr.com/ru/all/")

time.sleep(5)

locator = '[class="tm-svg-img tm-header-user-menu__icon tm-header-user-menu__icon_search"]'
element = driver.find_element(By.CSS_SELECTOR, locator)
element.click()

time.sleep(5)

driver.quit()
