class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        total = 0
        d = {0: 1}
        for x in nums:
            total += x
            if total - k in d:
                count += d[total - k]
            d[total] = d.get(total, 0) + 1
        return count