# Generate Parentheses

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given `n` pairs of parentheses, write a function to  *generate all combinations of well-formed parentheses*.

 

 **Example 1:** 

```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

```

 **Example 2:** 

```
Input: n = 1
Output: ["()"]

```

 

 **Constraints:** 

- 1 <= n <= 8

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 40.02%)  
**Memory:** 12.6 MB (beats 55.67%)  
**Submitted:** 2026-09-20T13:51:13.199Z  

```py
class Solution(object):
    def generateParenthesis(self, n):
        result = []
        current = []
        def backtrack(oc, cc):          
            if oc == n and cc == n:         # Base case
                result.append("".join(current))
                return          
            if oc < n:       # Add opening bracket
                current.append("(")
                backtrack(oc + 1, cc)
                current.pop()         
            if cc < oc:      # Add closing bracket
                current.append(")")
                backtrack(oc, cc + 1)
                current.pop()
        backtrack(0, 0)
        return result
```

---

[View on LeetCode](https://leetcode.com/problems/generate-parentheses/)