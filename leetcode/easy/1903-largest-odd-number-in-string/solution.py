class Solution(object):
    def largestOddNumber(self, num):
        n = len(num)
        for i in range(n):
            if int(num[i]) % 2 == 1:
                return num[i]
            