from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        numbers.sort()
        return numbers[0]