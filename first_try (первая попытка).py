from selenium.webdriver.chrome import webdriver
import time

driver = webdriver.WebDriver("chromedriver")

driver.get ("https://habr.com/ru/all/")

time.sleep(5)

driver.quit()
