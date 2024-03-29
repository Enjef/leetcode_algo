class Solution:
    # 52.01% 64.02%
    def commonFactors(self, a: int, b: int) -> int:
        res = 0
        for i in range(1, max(a, b)+1):
            if a % i == 0 and b % i == 0:
                res += 1
        return res
