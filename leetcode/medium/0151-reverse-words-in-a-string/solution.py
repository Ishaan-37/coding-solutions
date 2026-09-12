class Solution(object):
    def reverseWords(self, s):
        ans = ""
        for i in range(len(s)):
            return " ".join(s.split()[::-1])