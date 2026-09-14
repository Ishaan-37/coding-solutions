# Fibonacci Number

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

The  **Fibonacci numbers**, commonly denoted `F(n)` form a sequence, called the  **Fibonacci sequence**, such that each number is the sum of the two preceding ones, starting from `0` and `1`. That is,

```
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

```

Given `n`, calculate `F(n)`.

 

 **Example 1:** 

```
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

```

 **Example 2:** 

```
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

```

 **Example 3:** 

```
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

```

 

 **Constraints:** 

- 0 <= n <= 30

## Solution

**Language:** Python  
**Runtime:** 596 ms (beats 34.47%)  
**Memory:** 12.6 MB (beats 17.77%)  
**Submitted:** 2026-09-14T18:25:24.563Z  

```py
class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)
        
```

---

[View on LeetCode](https://leetcode.com/problems/fibonacci-number/)