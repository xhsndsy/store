import unittest
from ddt import ddt, data, unpack
from narcissistic_number import narcissistic_num


@ddt
class NarNumTestCase(unittest.TestCase):
    def setUp(self):
        print('test method start...')

    @data([135, '这个数不是水仙花数'], [-1, '这个数不在100到1000之内'], [153, '这个数是水仙花数'])
    @unpack
    def test_nar_num(self, n, expect):  # n为要输入的数,expect为预期结果
        result = narcissistic_num(n)
        self.assertEqual(result, expect, msg=result)
    def tearDown(self):
        print('test method end...')


if __name__ == '__main__':
    unittest.main(verbosity=2)