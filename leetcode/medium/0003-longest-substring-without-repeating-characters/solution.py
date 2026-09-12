class Solution(object):
    def lengthOfLongestSubstring(self, s):
        d = {}
        start = 0
        ans = 0
        for i in range(len(s)):
            ch = s[i]
            if ch in d and d[ch] >= start:
                start = d[ch] + 1
            d[ch] = i
            length = i - start + 1
            ans = max(ans, length)
        return ans