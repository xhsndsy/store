'''
    功能自动化适应场景：
        1.前提条件：在需求和功能变更的不是特别频繁的情况下是可以使用自动化来做测试。
            好处：节省人力资源。物力资源。
            缺点：对测试人员技术能力比较高。
        2.什么阶段进行的？
            性能测试之前，接口测试之后！
    3.环境搭建！
        1.联网安装selenium框架
        2.放好chromeDriver.exe驱动放在python的安装目录。
    浏览器的准备：
        1.谷歌，火狐
    浏览器的基本操作：
        1.找到输入框输入数据
        2.点击按钮
            driver.find_element_by_id().click
            send_keys()
            clear()
        3.鼠标滑动，其他的鼠标操作。
        4.使用花样定位方式来定位元素。
            driver.find_element_by_id()
            find_element_by_name()
            find_element_by_xpath()
        5.截图操作：
            save_screenshot()

任务1：
    京东的搜索一个商品，点击详情，添加购物车。
    实现苏宁的搜索和点击详情，添加购物车。

    b站登陆，搜索一个鬼畜素材。




'''

from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get(r"F:/自动化测试20组/练习的html/frame.html")

driver.maximize_window()

# driver.find_element_by_id("input1").send_keys("jason")

#xpath：绝对定位，相对定位
driver.find_element("//*[@id='input1']").send_keys("jason")

driver.save_screenshot("登陆.jpg")






time.sleep(3)

driver.quit()














































































