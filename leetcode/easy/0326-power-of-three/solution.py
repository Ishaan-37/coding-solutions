class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 2:
            return False
        if n % 3 == 0:
            n = n // 3
            return True