class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:  # 89.15% 75.76%
        if not s:
            return True
        j = 0
        for char in t:
            if char == s[j]:
                j += 1
            if j == len(s):
                return True
        return False
