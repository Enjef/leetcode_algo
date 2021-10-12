class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        nums.sort()
        diff = 0
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] > diff:
                diff = nums[i+1] - nums[i]
        return diff
