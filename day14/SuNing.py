from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get('https://www.suning.com/')

driver.maximize_window()

driver.find_element(By.XPATH, '//*[@id="searchKeywords"]').send_keys('Y9000')
driver.find_element(By.XPATH, '//*[@id="searchSubmit"]').click()
driver.find_element(By.XPATH, '//*[@id="ssdsn_search_pro_baoguang-1-0-1_1_01:0010329931_12309524278"]/img').click()

time.sleep(20)
driver.find_element(By.CSS_SELECTOR, 'document.querySelector("#addCart")').click()


