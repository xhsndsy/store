import time

from selenium.webdriver.common.by import By


class Login_Operation:

    def __init__(self, driver):
        self.driver = driver

    def Login(self, username, password) :

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='loginname']").send_keys(username)
        
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(password)
        
        self.driver.find_element(By.XPATH, "//*[@id='submit']").click()


    def getSuccessResult(self):
        return self.driver.title

    def getErrorResult(self):
        return self.driver.find_element(By.XPATH, "//*[@id='msg_uname']").text