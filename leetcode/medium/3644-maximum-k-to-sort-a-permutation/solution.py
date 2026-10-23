class Solution(object):
    def sortPermutation(self, nums):
        n = len(nums)
        if nums == sorted(nums):
            return 0
        k = -1
        for i in range(n):
            if nums[i] != i:
                k &= nums[i]
        return k