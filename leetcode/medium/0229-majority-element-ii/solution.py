class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        d = {}
        ans = []
        for ch in nums:
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] = d[ch]+1
        for ch in d:
            if d[ch] > n//3 :
                ans.append(ch)
        return ans