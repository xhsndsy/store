#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 如果目标值存在返回下标，否则返回 -1
# @param nums int整型一维数组
# @param target int整型
# @return int整型
#
from typing import List


class Solution:
    def search(self , nums: List[int], target: int) -> int:
        # write code here
        if not nums:
            return -1
        n = len(nums)
        mid = int(n/2)
        if target not in nums:
            return -1
        while True:
            if nums[mid] > target:
                mid = mid - 1
            if nums[mid] < target:
                mid = mid + 1
            if nums[mid] == target:
                if nums[mid] == nums[mid - 1]:
                    if mid == 0:
                        return mid
                    else:
                        mid -= 1
                else:
                    return mid


s = Solution()
print(s.search([-2, -2, -2, -2, -2], -2))