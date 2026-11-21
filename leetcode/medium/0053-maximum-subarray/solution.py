class Solution(object):
    def maxSubArray(self, nums):
        max_sum = nums[0]
        curr_sum = nums[0]       
        for i in nums[1:]:
            curr_sum = max(i, curr_sum + i)
            max_sum = max(max_sum, curr_sum)          
        return max_sum