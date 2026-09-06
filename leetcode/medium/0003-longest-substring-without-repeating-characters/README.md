# Longest Substring Without Repeating Characters

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string `s`, find the length of the  **longest**   **substring**  without duplicate characters.

 

 **Example 1:** 

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

```

 **Example 2:** 

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

```

 **Example 3:** 

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

```

 

 **Constraints:** 

- 0 <= s.length <= 105
- s consists of English letters, digits, symbols and spaces.

## Solution

**Language:** Python  
**Runtime:** 327 ms (beats 46.34%)  
**Memory:** 16.6 MB (beats 36.60%)  
**Submitted:** 2026-09-06T08:52:18.842Z  

```py
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        ans = 0
        d ={}
        for right in range(len(s)):
            if s[right] in d:
                left = max(left, d[s[right]] + 1)
            d[s[right]] = right
            ans = max(ans, right - left + 1)
        return ans
```

---

[View on LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)