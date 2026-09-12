class Solution(object):
    def removeOuterParentheses(self, s):
        ans = ""
        count = 0
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
                if count > 1:
                    ans += s[i]
            else:
                count -= 1
                if count > 0:
                    ans += s[i]

        return ans