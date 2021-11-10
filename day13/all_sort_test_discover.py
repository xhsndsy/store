# 批量测试用例
import unittest
from day13 import HTMLTestRunner
import os

sort_path = os.path.dirname(os.path.realpath(__file__))
reprort_path = os.path.join(sort_path, '../report')
if not os.path.exists(reprort_path):os.mkdir(reprort_path)

test_dir = '../'
suite = unittest.TestLoader().discover(test_dir, pattern='*sort.py')
# *test.py 代表所有可测试文件

if __name__ == "__main__":
    html_report = reprort_path + r"\result.html"
    fp = open(html_report, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="单元测试报告", description="用例执行情况")
    runner.run(suite)