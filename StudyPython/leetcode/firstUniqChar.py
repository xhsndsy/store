class Solution:
    def firstUniqChar(self, s: str) -> str:
        dict = {}
        for i in s:
            dict[i] = dict.get(i,0)+1
        for i in s:
            if dict[i] == 1:
                return i

        return ' '