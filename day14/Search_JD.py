from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

Driver = webdriver.Chrome()

Driver.get('https://www.jd.com')

Driver.maximize_window()

Driver.find_element(By.XPATH, '//*[@id="key"]').send_keys('thinkpad e480')

Driver.find_element(By.XPATH, '//*[@id="search"]/div/div[2]/button').click()

Driver.find_element(By.XPATH, '//*[@id="J_goodsList"]/ul/li[2]/div/div[1]/a/img').click()

Driver.find_element(By.XPATH, '//*[@id="choose-attr-1"]/div[2]/div[6]/a').click()

Driver.find_element(By.XPATH, '//*[@id="choose-attr-2"]/div[2]/div[4]/a').click()

Driver.find_element(By.XPATH, '//*[@id="InitCartUrl"]').click()
#

Driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]').click()

Driver.find_element(By.XPATH, '//*[@id="loginname"]').send_keys('18942674117')

Driver.find_element(By.XPATH, '//*[@id="nloginpwd"]').send_keys('hzj522zy.')

Driver.find_element(By.XPATH, '//*[@id="loginsubmit"]').click()






# 找到该滑块
button = Driver.find_element(By.XPATH, '//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[3]')

action = ActionChains(Driver)            # 实例化一个action对象

while True:
    time.sleep(1)
    action.click_and_hold(button)

    action.move_by_offset(100, 0)

    action.release().perform()





# perform()用来执行ActionChains中存储的行为

# 移动滑块

