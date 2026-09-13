class Solution(object):
    def peakIndexInMountainArray(self, arr):
        n = len(arr)
        for i in range(n):
            return arr.index(max(arr))