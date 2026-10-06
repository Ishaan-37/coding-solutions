class Solution(object):
    def minAddToMakeValid(self, s):
        ans = 0
        depth = 0
        for ch in s:
            if ch == '(':
                depth += 1
            else:
                depth -= 1
            if depth < 0:
                ans += 1
                depth = 0
        return ans + depth