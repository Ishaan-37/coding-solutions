class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        nums.sort()
        d = {}
        for num in nums:
            d[num] = d.get(num,0) + 1
            if d[num] > n/2:
                return num