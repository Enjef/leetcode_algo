class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = left + (right - left) // 2
            if mid*mid == x:
                return mid
            if mid*mid < x:
                left = mid + 1
            else:
                right = mid - 1
        if mid*mid > x:
            return mid - 1
        return mid


x = Solution()
print(x.mySqrt(17))
