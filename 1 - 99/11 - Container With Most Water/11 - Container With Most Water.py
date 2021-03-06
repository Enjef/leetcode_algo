class Solution:
    def maxArea(self, height) -> int:  # 56.78% 94.71%
        v_max = float('-inf')
        left = 0
        right = len(height) - 1
        if len(height) == 2:
            return min(height[0], height[1])
        while left < right:
            v_max = max(v_max, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return v_max

    def maxArea_study_plan(self, height: List[int]) -> int:  # 30.19% 57.02%
        i, j = 0, len(height) - 1
        v_max = 0
        while i < j:
            v_max = max(v_max, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return v_max

    def maxArea_best_speed_new(self, height) -> int:
        def area(left, right):
            w = right - left
            h = min(height[left], height[right])
            return h * w
        max_area = 0
        left_pointer, right_pointer = 0, len(height) - 1
        max_height = max(height)
        while left_pointer < right_pointer:
            max_area = max(max_area, area(left_pointer, right_pointer))
            if max_height * (right_pointer - left_pointer) < max_area:
                break
            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
        return max_area

    def maxArea_best_speed(self, height: List[int]) -> int:
        res = 0
        r = len(height) - 1
        l = 0
        hmax = max(height)
        while (r - l) * hmax >= res:
            res = max(res, min(height[l], height[r])*(r-l))
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return res
