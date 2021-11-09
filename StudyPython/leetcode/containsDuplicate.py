from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = []

        for i in nums:
            if i in res:
                return True
            res.append(i)
        return False


s = Solution()

print(s.containsDuplicate([1, 2, 3, 1]))