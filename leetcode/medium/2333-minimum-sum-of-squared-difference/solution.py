
class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diffs) <= k:
            return 0

        left, right = 0, max(diffs)

        # Find the smallest maximum difference
        # achievable within k operations
        while left < right:
            mid = (left + right) // 2

            ops = sum(max(d - mid, 0) for d in diffs)

            if ops <= k:
                right = mid
            else:
                left = mid + 1

        limit = left

        # Reduce all differences to at most limit
        ops = sum(max(d - limit, 0) for d in diffs)
        remaining = k - ops

        # Calculate squared sum after capping differences
        ans = sum(min(d, limit) ** 2 for d in diffs)

        # Use remaining operations to reduce limit to limit - 1
        ans -= remaining * (2 * limit - 1)

        return ans
