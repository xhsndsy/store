import unittest
from ddt import ddt, data, unpack
from dichotomy_sort import foo


@ddt
class DichotomySortTestCase(unittest.TestCase):
    def setUp(self):
        print('test method start...')

    @data([list(range(13)), 8, 8], [list(range(10)), 9, 9], [list(range(20)), 21, -1])
    @unpack
    def test_dichotomy_sort(self, x, k, expect):  # x,k为要输入的数,expect为预期结果
        result = foo(x, k)
        self.assertEqual(result, expect, msg=result)
    def tearDown(self):
        print('test method end...')


if __name__ == '__main__':
    unittest.main(verbosity=2)