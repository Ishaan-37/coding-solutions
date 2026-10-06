# Minimum Add to Make Parentheses Valid

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

A parentheses string is valid if and only if:

- It is the empty string,
- It can be written as AB (A concatenated with B), where A and B are valid strings, or
- It can be written as (A), where A is a valid string.

You are given a parentheses string `s`. In one move, you can insert a parenthesis at any position of the string.

- For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".

Return  *the minimum number of moves required to make* `s` *valid*.

 

 **Example 1:** 

```
Input: s = "())"
Output: 1

```

 **Example 2:** 

```
Input: s = "((("
Output: 3

```

 

 **Constraints:** 

- 1 <= s.length <= 1000
- s[i] is either '(' or ')'.

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 12.3 MB (beats 56.02%)  
**Submitted:** 2026-10-06T06:01:52.606Z  

```py
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
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)