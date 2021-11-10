import unittest
from day13.sort1 import sjx
from ddt import ddt, data, unpack


@ddt
class SoftTestCase(unittest.TestCase):
    def setUp(self):
        print('test method start...')

    @data([1, 1, 1, '这个三角形是等边三角形'], [1, 2, 2, '等腰三角形'], [3, 4, 5, '一般三角形'], [1, 1, 2, '不是三角形'])
    @unpack
    def test_sjx(self, x, y, z, expect):  # x,y为要输入的数,expect为预期结果
        result = sjx(x, y, z)
        self.assertEqual(result, expect, msg=result)
        # asserNotEqual(A,B)判断两个值不相等
        # assertTure() 检验表达式时真值    assertFalse()检验表达式为假值
        # self.assertIn(a, b) 检验b是否包含a
        # self.assertGreater(a,b) a>b
        # self.assertGreaterEqual(a,b) a>=b
        # self.assertLess(a,b) a<b
        # self,assertLessEqual(a,b) a<=b
        # self.assertRegexpMatches(s,r) 检验文本是否符合正则匹配
        # 
    def tearDown(self):
        print('test method end...')


if __name__ == '__main__':
    unittest.main(verbosity=2)
