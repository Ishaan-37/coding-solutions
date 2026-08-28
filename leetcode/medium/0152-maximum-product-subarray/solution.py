class Solution(object):
    def maxProduct(self, nums):
        max_prod = nums[0] 
        cur_max = nums[0]
        cur_min = nums[0]
        for n in nums[1:]:
            candidates = ( n, cur_max*n, cur_min*n )
            cur_max, cur_min = max(candidates), min(candidates)
            max_prod = max(max_prod, cur_max)
        return max_prod
        