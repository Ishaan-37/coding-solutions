# Minimum Insertions to Balance a Parentheses String

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a parentheses string `s` containing only the characters `'('` and `')'`. A parentheses string is  **balanced**  if:

- Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
- Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.

In other words, we treat `'('` as an opening parenthesis and `'))'` as a closing parenthesis.

- For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.

You can insert the characters `'('` and `')'` at any position of the string to balance it if needed.

Return  *the minimum number of insertions*  needed to make `s` balanced.

 

 **Example 1:** 

```
Input: s = "(()))"
Output: 1
Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. We need to add one more ')' at the end of the string to be "(())))" which is balanced.

```

 **Example 2:** 

```
Input: s = "())"
Output: 0
Explanation: The string is already balanced.

```

 **Example 3:** 

```
Input: s = "))())("
Output: 3
Explanation: Add '(' to match the first '))', Add '))' to match the last '('.

```

 

 **Constraints:** 

- 1 <= s.length <= 105
- s consists of '(' and ')' only.

## Solution

**Language:** Python  
**Runtime:** 75 ms (beats 100.00%)  
**Memory:** 12.9 MB (beats 31.25%)  
**Submitted:** 2026-10-10T07:32:08.055Z  

```py

class Solution(object):
    def minInsertions(self, s):
        insertions = 0
        need = 0

        for ch in s:
            if ch == '(':
                # Previous opening bracket needs one more ')'
                if need % 2 == 1:
                    insertions += 1
                    need -= 1

                # Every '(' needs two ')'
                need += 2

            else:  # ch == ')'
                need -= 1

                # Extra ')' without a matching '('
                if need < 0:
                    insertions += 1
                    need = 1

        # Insert any missing closing brackets
        return insertions + need

```

---

[View on LeetCode](https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/)