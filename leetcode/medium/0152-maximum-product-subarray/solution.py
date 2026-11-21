class Solution(object):
    def maxProduct(self, nums):
        ans = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]
        for i in nums[1:]:
            if i < 0:
                curr_max, curr_min = curr_min, curr_max 
            curr_max = max(i, curr_max * i)
            curr_min = min(i, curr_min * i)
            ans = max(ans, curr_max)
        return ans               