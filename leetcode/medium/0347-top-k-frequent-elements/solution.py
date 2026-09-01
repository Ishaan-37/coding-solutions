class Solution(object):
    def topKFrequent(self, nums, k):
        d = {}
        for num in nums:
            d[num] = d.get(num,0)+1
        return sorted(d, key=d.get, reverse=True)[:k]
        