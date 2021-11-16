#F:/自动化测试20组/练习的html/上传文件和下拉列表/autotest.html
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get(r"F:/自动化测试20组/练习的html/上传文件和下拉列表/autotest.html")

driver.maximize_window()

driver.find_element_by_xpath("//input[@name='account' and @type='text']").send_keys("jason")

driver.find_element_by_xpath("//input[@name='password' and @type='password']").send_keys("admin")

driver.find_element_by_xpath("//*[@id='areaID']").send_keys("北京市")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='sexID2']").click()

# 选择春天，秋天
time.sleep(1)
driver.find_element_by_xpath("//*[@value='spring']").click()
driver.find_element_by_xpath("//*[@value='Auterm']").click()

time.sleep(1)

# 上传文件
driver.find_element_by_xpath("//*[@name='file' and @type='file']").send_keys(r"C:\Users\jason\Pictures\picture.jpg")


time.sleep(2)
driver.quit()



