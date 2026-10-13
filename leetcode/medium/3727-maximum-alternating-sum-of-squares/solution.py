class Solution(object):
    def maxAlternatingSum(self, nums):
        nums.sort(key=abs)
        n = len(nums)
        score = 0

        for i in range(n // 2):
            score -= nums[i] * nums[i]

        for i in range(n // 2, n):
            score += nums[i] * nums[i]

        return score