# First Unique Character in a String

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string `s`, find the  **first**  non-repeating character in it and return its index. If it  **does not**  exist, return `-1`.

 

 **Example 1:** 

 **Input:**  s = "leetcode"

 **Output:**  0

 **Explanation:** 

The character `'l'` at index 0 is the first character that does not occur at any other index.

 **Example 2:** 

 **Input:**  s = "loveleetcode"

 **Output:**  2

 **Example 3:** 

 **Input:**  s = "aabb"

 **Output:**  -1

 

 **Constraints:** 

- 1 <= s.length <= 105
- s consists of only lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 96 ms (beats 68.12%)  
**Memory:** 15.7 MB (beats 38.90%)  
**Submitted:** 2026-09-02T06:52:58.873Z  

```py
class Solution(object):
    def firstUniqChar(self, s):
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch,0)+1
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i
        return -1

```

---

[View on LeetCode](https://leetcode.com/problems/first-unique-character-in-a-string/)