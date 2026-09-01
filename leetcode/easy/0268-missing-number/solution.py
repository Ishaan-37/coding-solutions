class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        for num in range(n + 1):
            if num not in nums:
                return num
        
        