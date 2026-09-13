class Solution:
    def findKRotation(self, arr):
        n = len(arr)
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                return i+1
        return 0
        