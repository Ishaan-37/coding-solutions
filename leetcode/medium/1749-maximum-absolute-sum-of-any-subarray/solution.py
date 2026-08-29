class Solution(object):
    def maxAbsoluteSum(self, nums):
        max_sum = cur_max = 0
        for n in nums:
            cur_max = max(0, cur_max + n)
            max_sum = max(max_sum, cur_max)
        min_sum = cur_min = 0
        for n in nums:
            cur_min = min(0, cur_min + n)
            min_sum = min(min_sum, cur_min)

        return max(max_sum, abs(min_sum))  
        