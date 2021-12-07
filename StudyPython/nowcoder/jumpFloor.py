#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param number int整型
# @return int整型
#
class Solution:
    def jumpFloor(self , number: int) -> int:
        if number <= 2:
            return number
        a = 0
        b = 1
        c = 0

        for _ in range(3, number-1):
            c = a + b
            a = b
            b = c
        return c