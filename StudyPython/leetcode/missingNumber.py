from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            if i in nums:
                pass
            else:
                return i


# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         return sum(range(len(nums) + 1)) - sum(nums)
