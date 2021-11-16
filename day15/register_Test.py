import time
from unittest import TestCase

from ddt import ddt, data, unpack
from selenium import webdriver
from selenium.webdriver.common.by import By


excpt = 'HKR.注册'

expect = 'HKR.注册'

step_one = '年龄仅支持15 到 75岁之间!'

account = 'xhsndsy'
name = '张源'
password = 'hzj522zy.'
twice_psd = 'hzj522zy.'

@ddt
class register_Testcase(TestCase):
    def setUp(self):
        print('test method start...')

    @data([excpt])
    @unpack
    def test_jinru(self, expect):
        driver = webdriver.Chrome()

        driver.get('http://localhost:8080/HKR/')
        driver.maximize_window()

        driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[2]/a[1]').click()

        time.sleep(3)
        title = driver.title

        driver.quit()
        self.assertEqual(title, expect, msg=title)

    @data([step_one])
    @unpack
    def test_register_step_one(self, stepone):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('http://localhost:8080/HKR/register.jsp')
        driver.find_element(By.XPATH, '//*[@id="loginname"]').send_keys(account)
        driver.find_element(By.XPATH, '//*[@id="msform"]/fieldset[1]/input[2]').send_keys(name)
        driver.find_element(By.XPATH, '//*[@id="pwd"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="msform"]/fieldset[1]/input[4]').send_keys(twice_psd)
        driver.find_element(By.XPATH, '//*[@id="msform"]/fieldset[1]/input[5]').click()
        driver.find_element(By.XPATH, '//*[@id="valid_age"]').send_keys(12)
        driver.find_element(By.XPATH, '//*[@id="msform"]/fieldset[1]/input[5]').click()

        alert = driver._switch_to.alert

        self.assertEqual(step_one, alert.text, msg=step_one)

    def tearDown(self) -> None:
        print('test method end')