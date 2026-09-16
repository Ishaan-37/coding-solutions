class Solution(object):
    def maxDepth(self, s):
       count = 0
       ans = 0 
       for ch in s:
        if ch == '(':
            count += 1
            ans = max(ans, count)
        if ch == ')':
            count -= 1
       return ans