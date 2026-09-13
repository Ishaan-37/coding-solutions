class Solution(object):
    def findPeakElement(self, nums):
        n = len(nums)
        for i in range(n):
            return nums.index(max(nums))