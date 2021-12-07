#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# lru design
# @param operators int整型二维数组 the ops
# @param k int整型 the k
# @return int整型一维数组

from typing import List


class Solution:
    def LRU(self, operators: List[List[int]], k: int) -> List[int]:
        # write code here
        res = {}
        while operators:
            tmp = operators.pop()
            opt = tmp[0]
            if opt == 1:
                res[tmp[1]] = tmp[2]

