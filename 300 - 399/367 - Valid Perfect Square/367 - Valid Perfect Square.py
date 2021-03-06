class Solution(object):
    def isPerfectSquare(self, num: int) -> bool:  # 39.94% 59.61%
        if num == 1:
            return True
        left = 1
        right = num//2
        while left <= right:
            mid = left + (right-left)//2
            cur = mid * mid
            if cur == num:
                return True
            if cur < num:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def isPerfectSquare_best_speed(self, n: int) -> bool:
      l = 1
      r = n
      while (l <= r):
        mid = l + (r-l) // 2
        if mid*mid == n:
          return True
        elif mid * mid < n:
          l = mid + 1
        else:
          r = mid - 1
      return False
