class Solution(object):
    def minOperations(self, nums):
        n = len(nums)
        arr = nums[:]
        for i in range(n):
            if arr == sorted(arr):
                return i
            if arr[::-1] == sorted(arr):
                return i + 1
            arr = arr[1:] + arr[:1]
        return -1