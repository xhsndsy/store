from typing import List

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            for j in i:
                if target == j:
                    return True
        else:
            return False


