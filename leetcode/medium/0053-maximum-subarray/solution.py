class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        curr = nums[0]
        prev = nums[0]
        for i in range(1, n):
            curr = max(nums[i], curr + nums[i])
            prev = max(prev, curr)
        return prev