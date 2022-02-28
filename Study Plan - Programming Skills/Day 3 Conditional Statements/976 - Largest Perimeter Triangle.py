class Solution:
    def largestPerimeter(self, nums: List[int]) -> int: # 80.08% 39.20%
        nums.sort()
        for i in range(len(nums)-1,1,-1):
            if nums[i-1] + nums[i-2] > nums[i]:
                return sum([nums[i-1], nums[i-2], nums[i]])
        return 0