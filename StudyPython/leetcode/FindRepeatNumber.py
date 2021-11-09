from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i in dic:
                return i
            dic[i] = 1

