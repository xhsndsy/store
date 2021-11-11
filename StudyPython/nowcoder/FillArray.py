class Solution:
    def FillArray(self, a, k):
        # write code here
        tmp = []
        for i in range(len(a)):
            num = []
            num.append(a[i])
            for j in range(1, k + 1):
                if a[i] == 0 and a[i - 1] <= j:
                    b = num.pop()
                    num.append(j)
            tmp.append(num)

        return tmp

s = Solution()


print(s.FillArray( [1, 0, 3, 0, 9], 9))