from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        count = 0
        for i in nums:
            if target == i:
                count += 1
        return count
