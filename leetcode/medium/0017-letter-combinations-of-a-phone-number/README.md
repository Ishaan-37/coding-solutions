# Letter Combinations of a Phone Number

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in  **any order**.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

 

 **Example 1:** 

```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

```

 **Example 2:** 

```
Input: digits = "2"
Output: ["a","b","c"]

```

 

 **Constraints:** 

- 1 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 12.4 MB (beats 59.20%)  
**Submitted:** 2026-09-20T17:28:00.963Z  

```py
class Solution(object):
    def letterCombinations(self, digits):
        mapping = {
            "2" : "abc" ,
            "3" : "def" ,
            "4" : "ghi" ,
            "5" : "jkl" ,
            "6" : "mno" ,
            "7" : "pqrs" ,
            "8" : "tuv" ,
            "9" : "wxyz" ,
        }
        path = []
        result = []
        def backtrack(i):
            if i == len(digits):
                result.append("".join(path))
                return
            for ch in mapping[digits[i]]:
                path.append(ch)
                backtrack(i+1)
                path.pop()
        backtrack(0)
        return result
```

---

[View on LeetCode](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)