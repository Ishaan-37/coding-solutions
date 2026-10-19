class Solution(object):
    def targetIndices(self, nums, target):
        n = len(nums)
        nums.sort()
        ans=[]
        for i in range(n):
            if nums[i] == target:     
                ans.append(i)
        return ans