class Solution(object):
    def merge(self, nums1, m, nums2, n):
        ans = nums1[:m] + nums2[:n]
        ans.sort()
        nums1[:] = ans