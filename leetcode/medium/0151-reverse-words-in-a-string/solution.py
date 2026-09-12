class Solution(object):
    def reverseWords(self, s):
        for i in range(len(s)):
            return " ".join(s.split()[::-1])