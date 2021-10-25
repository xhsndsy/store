import unittest
from ddt import ddt, data, unpack
from bubble_sort_test import bubble_sortTestCase
import HTMLTestRunner
import os

sort_path = os.path.dirname(os.path.realpath(__file__))
reprort_path = os.path.join(sort_path, 'report')
if not os.path.exists(reprort_path):os.mkdir(reprort_path)

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(bubble_sortTestCase))


if __name__ == "__main__":
    html_report = reprort_path + r"\result.html"
    fp = open(html_report, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="单元测试报告", description="用例执行情况")
    runner.run(suite)