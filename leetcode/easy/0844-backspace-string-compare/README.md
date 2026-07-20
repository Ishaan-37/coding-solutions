# Backspace String Compare

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two strings `s` and `t`, return `true`  *if they are equal when both are typed into empty text editors*. `'#'` means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

 **Example 1:** 

```
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

```

 **Example 2:** 

```
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

```

 **Example 3:** 

```
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

```

 

 **Constraints:** 

- 1 <= s.length, t.length <= 200
- s and t only contain lowercase letters and '#' characters.

 

 **Follow up:**  Can you solve it in `O(n)` time and `O(1)` space?

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 12.5 MB (beats 18.51%)  
**Submitted:** 2026-07-20T19:48:48.212Z  

```py
class Solution:
    def backspaceCompare(self, s, t):

        # Pointers starting from the end
        i = len(s) - 1
        j = len(t) - 1

        while i >= 0 or j >= 0:

            # Find next valid character in s
            skip = 0
            while i >= 0:
                if s[i] == "#":
                    skip += 1
                    i -= 1
                elif skip > 0:
                    skip -= 1
                    i -= 1
                else:
                    break

            # Find next valid character in t
            skip = 0
            while j >= 0:
                if t[j] == "#":
                    skip += 1
                    j -= 1
                elif skip > 0:
                    skip -= 1
                    j -= 1
                else:
                    break

            # Compare current valid characters
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False

            # One string has a character left, the other doesn't
            elif i >= 0 or j >= 0:
                return False

            # Move to previous character
            i -= 1
            j -= 1

        return True
```

---

[View on LeetCode](https://leetcode.com/problems/backspace-string-compare/)