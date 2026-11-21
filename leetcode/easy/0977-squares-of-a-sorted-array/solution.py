class Solution(object):
    def sortedSquares(self, nums):
        import math
        ans = [int(math.pow(x, 2)) for x in nums]
        ans.sort()
        return ans
