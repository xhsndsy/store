from selenium import webdriver
from ddt import data, ddt, unpack
import unittest
from LoginOperation import Login_Operation
from datasource import InitPage

@ddt
class Tset_Login(unittest.TestCase):


    @data(*InitPage().getloginSuccessData())
    def test_Login_Success(self, login_success):
        name = login_success['name']
        password = login_success['password']
        expect = login_success['expect']

        driver = webdriver.Chrome()
        driver.get("http://localhost:8080/HKR")
        driver.maximize_window()

        login = Login_Operation(driver)

        login.Login(name, password)

        result = login.getSuccessResult()
        driver.quit()

        self.assertEqual(result, expect)

    @data(*InitPage().getloginErrorData())
    def test_Login_Error(self, login_error):
        name = login_error['name']
        password = login_error['password']
        expect = login_error['expect']

        driver = webdriver.Chrome()
        driver.get("http://localhost:8080/HKR")
        driver.maximize_window()

        login = Login_Operation(driver)

        login.Login(name, password)

        result = login.getErrorResult()
        driver.quit()

        self.assertEqual(result, expect)




if __name__ == '__main__':
    unittest.main(verbosity=2)
