class Solution(object):
    def maxSumOfSquares(self, num, sum):
        ans = ""
        for i in range(num):
            d = min(9, sum)
            ans += str(d)
            sum -= d
        if sum > 0:
            return ""
        return ans