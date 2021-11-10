import unittest
from ddt import ddt, data, unpack
from day13.bubble_sort import bubble_sort


@ddt
class bubble_sortTestCase(unittest.TestCase):
    def setUp(self):
        print('test method start...')

    @data([[10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21], [5, 7, 10, 15, 17, 21, 24, 27, 30, 36, 45, 50]], [[10, 17, 50, 7, 30, 24], [7, 10, 17, 24, 30, 50]], [[10, 17, 50, 7], [7, 10, 17, 50]])
    @unpack
    def test_sjx(self, x, expect):  # x,y为要输入的数,expect为预期结果
        result = bubble_sort(x)
        self.assertEqual(result, expect, msg=result)
    def tearDown(self):
        print('test method end...')


if __name__ == '__main__':
    unittest.main(verbosity=2)
