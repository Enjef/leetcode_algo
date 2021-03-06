class Solution:
    def searchInsert(self, nums, target: int) -> int:  # 11.69% 7.70%
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] > target:
                return i
        return len(nums)

    def searchInsert_v2(self, nums, target):  # 78.98% 85.73%
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
