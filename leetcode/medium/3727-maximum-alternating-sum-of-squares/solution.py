class Solution(object):
    def maxAlternatingSum(self, nums):
        ans = []
        n = len(nums)
         
        for num in nums:
            ans.append(num * num)
        ans.sort(reverse=True)                       
        score = 0
        for i in range(n):
            if i < (n + 1) // 2:
                score += ans[i]
            else:
                score -= ans[i]
        return score