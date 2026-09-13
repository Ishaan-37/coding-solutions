class Solution(object):
    def findMin(self, nums):
        n = len(nums)
        nums.sort()
        for i in range(n):
            return nums[i]