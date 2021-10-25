import unittest

from dichotomy_test_sort import DichotomySortTestCase
from insert_test_sort import InsertSortTestCase
from IsPrime_test_sort import IsPrimeTestCase
from narcissistic_number_test_sort import NarNumTestCase

import HTMLTestRunner
import os

sort_path = os.path.dirname(os.path.realpath(__file__))
reprort_path = os.path.join(sort_path, 'report')
if not os.path.exists(reprort_path):os.mkdir(reprort_path)

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(DichotomySortTestCase))
suite.addTest(unittest.makeSuite(InsertSortTestCase))
suite.addTest(unittest.makeSuite(IsPrimeTestCase))
suite.addTest(unittest.makeSuite(NarNumTestCase))


if __name__ == "__main__":
    html_report = reprort_path + r"\result2.html"
    fp = open(html_report, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="单元测试报告", description="用例执行情况")
    runner.run(suite)