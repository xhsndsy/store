from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        n1 = 0
        n2 = 0

        stack = []

        while True:
            if n1<len(nums1) and n2<len(nums2):
                if nums1[n1] == nums2[n2]:
                    stack.append(nums1[n1])
                    n1 += 1
                    n2 += 1
                elif nums1[n1] < nums2[n2]:
                    n1 += 1
                elif nums1[n1] > nums2[n2]:
                    n2 += 1
            else:
                break
        return stack

s = Solution()

print(s.intersect([1, 2, 2, 1], [2, 2]))