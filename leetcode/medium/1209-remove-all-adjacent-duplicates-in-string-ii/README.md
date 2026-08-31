# Remove All Adjacent Duplicates in String II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a string `s` and an integer `k`, a `k`  **duplicate removal**  consists of choosing `k` adjacent and equal letters from `s` and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make `k`  **duplicate removals**  on `s` until we no longer can.

Return  *the final string after all such duplicate removals have been made*. It is guaranteed that the answer is  **unique**.

 

 **Example 1:** 

```
Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
```

 **Example 2:** 

```
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
```

 **Example 3:** 

```
Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"

```

 

 **Constraints:** 

- 1 <= s.length <= 105
- 2 <= k <= 104
- s only contains lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 53 ms (beats 85.71%)  
**Memory:** 18.1 MB (beats 87.53%)  
**Submitted:** 2026-08-31T15:44:37.791Z  

```py
class Solution(object):
    def removeDuplicates(self, s, k):
        stack = []

        for x in s:
            if stack and stack[-1][0] == x:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([x, 1])

        return ''.join(x * count for x, count in stack)
```

---

[View on LeetCode](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/)