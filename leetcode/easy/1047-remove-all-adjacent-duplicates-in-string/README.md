# Remove All Adjacent Duplicates In String

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given a string `s` consisting of lowercase English letters. A  **duplicate removal**  consists of choosing two  **adjacent**  and  **equal**  letters and removing them.

We repeatedly make  **duplicate removals**  on `s` until we no longer can.

Return  *the final string after all such duplicate removals have been made*. It can be proven that the answer is  **unique**.

 

 **Example 1:** 

```
Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

```

 **Example 2:** 

```
Input: s = "azxxzy"
Output: "ay"

```

 

 **Constraints:** 

- 1 <= s.length <= 105
- s consists of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 33 ms (beats 91.31%)  
**Memory:** 13.4 MB (beats 89.86%)  
**Submitted:** 2026-08-31T08:33:15.901Z  

```py
class Solution(object):
    def removeDuplicates(self, s):
        stack = []
        for x in s:
            if stack and stack[-1] == x:
                stack.pop()
            else:
                stack.append(x)
        return''.join(stack)
```

---

[View on LeetCode](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)