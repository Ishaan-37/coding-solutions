# Valid Palindrome

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

A phrase is a  **palindrome**  if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` *if it is a  **palindrome**, or* `false` *otherwise*.

 

 **Example 1:** 

```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

```

 **Example 2:** 

```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

```

 **Example 3:** 

```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

```

 

 **Constraints:** 

- 1 <= s.length <= 2 * 105
- s consists only of printable ASCII characters.

## Solution

**Language:** Python  
**Runtime:** 15 ms (beats 71.97%)  
**Memory:** 12.5 MB (beats 91.63%)  
**Submitted:** 2026-08-17T07:36:20.221Z  

```py
class Solution(object):
    def isPalindrome(self, s):
        start = 0
        end = len(s) - 1
        while start < end:
            if not s[start].isalnum():
             start += 1

            elif not s[end].isalnum():
             end -= 1

            elif s[start].lower() != s[end].lower():
             return False

            else:
             start += 1
             end -= 1

        return True
            

        
```

---

[View on LeetCode](https://leetcode.com/problems/valid-palindrome/)