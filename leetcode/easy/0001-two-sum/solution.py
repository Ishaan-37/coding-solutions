class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        ch = {}
        for i in range(n):
            difference = target - nums[i]
            if difference in ch:
                return [ ch[difference], i ]
            ch[nums[i]] = i