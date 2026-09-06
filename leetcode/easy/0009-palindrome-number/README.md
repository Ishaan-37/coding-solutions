# Palindrome Number

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer `x`, return `true` if `x` is a  **palindrome**, and `false` otherwise.

 

 **Example 1:** 

```
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

```

 **Example 2:** 

```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

```

 **Example 3:** 

```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

```

 

 **Constraints:** 

- -231 <= x <= 231 - 1

 

 **Follow up:**  Could you solve it without converting the integer to a string?

## Solution

**Language:** Python  
**Runtime:** 27 ms (beats 6.89%)  
**Memory:** 12.4 MB (beats 18.77%)  
**Submitted:** 2026-09-06T10:07:27.686Z  

```py
class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        for i in range(len(x)):
            if x[i] != x[-i-1]:
                return False 
        else:
            return True
```

---

[View on LeetCode](https://leetcode.com/problems/palindrome-number/)