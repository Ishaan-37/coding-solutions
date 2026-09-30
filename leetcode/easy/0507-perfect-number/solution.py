class Solution(object):
    def checkPerfectNumber(self, num):
        ans = 0 
        for i in range(1, num):
            if num % i == 0:
                ans += i
        return ans == num