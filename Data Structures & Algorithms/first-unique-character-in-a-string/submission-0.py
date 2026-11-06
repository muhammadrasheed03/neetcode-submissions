class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}

        for c in s:
            count[c] = count.get(c,0)+1

        for i, char in enumerate(s):
            if count[char]==1:
                return i
        return -1

        