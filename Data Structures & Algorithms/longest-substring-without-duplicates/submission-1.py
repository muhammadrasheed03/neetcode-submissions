class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        best = 0
        left = 0

        for right, char in enumerate(s):
            while char in seen:
                seen.remove(s[left])

                left+=1
            seen.add(char)
            best = max(best, right-left+1)

        return best