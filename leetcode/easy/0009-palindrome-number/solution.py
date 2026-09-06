class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        for i in range(len(x)):
            if x[i] != x[-i-1]:
                return False 
        else:
            return True