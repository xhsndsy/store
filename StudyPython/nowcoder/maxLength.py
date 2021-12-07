#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def maxLength(self , arr ):
        l = []
        m = 0
        n = 0
        for i in arr:
            if i not in l:
                l.append(i)
                n += 1
            else:
                m = max(m, n)
                l = l[l.index(i)+1:]
                l.append(i)
                n = len(l)
        return max(m,n)
