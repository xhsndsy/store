import unittest
from ddt import ddt, data, unpack
from day13.isPirme import IsPrime


@ddt
class IsPrimeTestCase(unittest.TestCase):
    def setUp(self):
        print('test method start...')

    @data([1, '此函数不是素数'], [11, '此函数是素数'], [-1, '此函数不是素数'])
    @unpack
    def test_is_prime(self, n, expect):  # n为要输入的数,expect为预期结果
        result = IsPrime(n)
        self.assertEqual(result, expect, msg=result)
    def tearDown(self):
        print('test method end...')


if __name__ == '__main__':
    unittest.main(verbosity=2)