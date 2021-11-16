import time
import unittest

from ddt import ddt, data, unpack
from selenium import webdriver
from selenium.webdriver.common.by import By

account = 'xhsndsy'
password = 'hzj522zy.'

class Test_User(unittest.TestCase):

    def setUp(self) -> None:
        print('开始执行用例')

    def test_Modify(self):



        driver = webdriver.Chrome()

        driver.get('http://localhost:8080/HKR/')

        driver.find_element(By.XPATH, '//*[@id="loginname"]').send_keys(account)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="submit"]').click()
        driver.maximize_window()
        driver.find_element(By.XPATH, '//*[@id="img"]').click()

        time.sleep(4)
        driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[2]/div/div[3]/ul/li[4]/img').click()
        time.sleep(2)
        text = driver.find_element(By.XPATH, '/html/body/div[7]').text

        self.assertEqual(text, '操作提示\n成功修改头像!')

    def test_upload(self):
        driver = webdriver.Chrome()
        driver.get('http://localhost:8080/HKR/')
        driver.find_element(By.XPATH, '//*[@id="loginname"]').send_keys(account)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="submit"]').click()
        driver.maximize_window()
        driver.find_element(By.XPATH, '//*[@id="img"]').click()
        driver.find_element(By.XPATH, '//*[@id="lablefile"]"]').click()



    def tearDown(self) -> None:
        print('用例执行结束')


