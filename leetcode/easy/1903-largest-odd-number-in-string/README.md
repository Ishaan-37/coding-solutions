# Largest Odd Number in String

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given a string `num`, representing a large integer. Return  *the  **largest-valued odd**  integer (as a string) that is a  **non-empty substring**  of* `num` *, or an empty string* `""` *if no odd integer exists*.

A  **substring**  is a contiguous sequence of characters within a string.

 

 **Example 1:** 

```
Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.

```

 **Example 2:** 

```
Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".

```

 **Example 3:** 

```
Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number.

```

 

 **Constraints:** 

- 1 <= num.length <= 105
- num only consists of digits and does not contain any leading zeros.

## Solution

**Language:** Python  
**Runtime:** 39 ms (beats 40.45%)  
**Memory:** 16.9 MB (beats 64.47%)  
**Submitted:** 2026-09-07T20:21:46.459Z  

```py
class Solution(object):
    def largestOddNumber(self, num):
        for i in range(len(num)-1, -1, -1):
            if int(num[i]) % 2:
                return num[:i+1]
        return ""
```

---

[View on LeetCode](https://leetcode.com/problems/largest-odd-number-in-string/)