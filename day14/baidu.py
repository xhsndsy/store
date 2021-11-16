
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

chromeDriver = webdriver.Chrome()


# 打开百度网址
chromeDriver.get("http://www.baidu.com")

# 窗口最大化
chromeDriver.maximize_window()

#寻找搜索输入框

# 点击百度一下按钮
chromeDriver.find_element(By.ID, 'su').click()

time.sleep(3)
# 退出浏览器
chromeDriver.quit()
chromeDriver.close()
