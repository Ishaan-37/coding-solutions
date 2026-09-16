# Maximum Nesting Depth of the Parentheses

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a  **valid parentheses string**  `s`, return the  **nesting depth**  of `s`. The nesting depth is the  **maximum**  number of nested parentheses.

 

 **Example 1:** 

 **Input:**  s = "(1+(2*3)+((8)/4))+1"

 **Output:**  3

 **Explanation:** 

Digit 8 is inside of 3 nested parentheses in the string.

 **Example 2:** 

 **Input:**  s = "(1)+((2))+(((3)))"

 **Output:**  3

 **Explanation:** 

Digit 3 is inside of 3 nested parentheses in the string.

 **Example 3:** 

 **Input:**  s = "()(())((()()))"

 **Output:**  3

 

 **Constraints:** 

- 1 <= s.length <= 100
- s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
- It is guaranteed that parentheses expression s is a VPS.

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 17.68%)  
**Memory:** 12.4 MB (beats 57.47%)  
**Submitted:** 2026-09-16T17:24:40.845Z  

```py
class Solution(object):
    def maxDepth(self, s):
       count = 0
       ans = 0 
       for ch in s:
        if ch == '(':
            count += 1
            ans = max(ans, count)
        if ch == ')':
            count -= 1
       return ans
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/)