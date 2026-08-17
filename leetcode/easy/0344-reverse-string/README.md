# Reverse String

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array in-place with `O(1)` extra memory.

 

 **Example 1:** 

```
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

```

 **Example 2:** 

```
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

```

 

 **Constraints:** 

- 1 <= s.length <= 105
- s[i] is a printable ascii character.

## Solution

**Language:** Python  
**Runtime:** 4 ms (beats 39.28%)  
**Memory:** 19.9 MB (beats 43.39%)  
**Submitted:** 2026-08-17T06:02:11.804Z  

```py
class Solution(object):
    def reverseString(self, s):
        start = 0
        end = len(s)-1
        while start < end:
            s[start],s[end] = s[end],s[start]
            start += 1
            end -= 1
        return s
        
        
```

---

[View on LeetCode](https://leetcode.com/problems/reverse-string/)