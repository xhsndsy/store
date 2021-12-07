#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param input int整型一维数组
# @param k int整型
# @return int整型一维数组
#
class Solution:
    def GetLeastNumbers_Solution(self, input: List[int], k: int) -> List[int]:
        # write code here
        input.sort()
        res = []

        for i in input:
            if i <= k:
                res.append(i)
        return res