class Solution(object):
    def findMaxAverage(self, nums, k):
        left = 0
        window_sum = 0
        ans = float("-inf")
        for right in range(len(nums)):
            window_sum += nums[right]
            if right - left + 1 == k:
                ans = max(ans,window_sum)
                window_sum -= nums[left]
                left +=1
        return ans / float(k) 


        