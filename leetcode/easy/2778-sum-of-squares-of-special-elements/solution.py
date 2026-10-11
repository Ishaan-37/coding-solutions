class Solution(object):
    def sumOfSquares(self, nums):
        n = len(nums)
        total = 0
        for i in range(len(nums)):
            if n % (i + 1) == 0:
                total += nums[i] * nums[i]
        return total