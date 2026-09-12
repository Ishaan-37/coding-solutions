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
**Runtime:** 273 ms (beats 60.81%)  
**Memory:** 16.8 MB (beats 25.34%)  
**Submitted:** 2026-09-12T19:57:01.824Z  

```py
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
```

---

[View on LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)