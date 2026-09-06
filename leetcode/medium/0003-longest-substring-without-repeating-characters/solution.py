class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        ans = 0
        d ={}
        for right in range(len(s)):
            if s[right] in d:
                left = max(d[s[right]] + 1)
                d[s[right]] = right
            ans = max(ans, right - left + 1)
        return ans