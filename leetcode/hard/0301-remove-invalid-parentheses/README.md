# Remove Invalid Parentheses

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given a string `s` that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return  *a list of  **unique strings**  that are valid with the minimum number of removals*. You may return the answer in  **any order**.

 

 **Example 1:** 

```
Input: s = "()())()"
Output: ["(())()","()()()"]

```

 **Example 2:** 

```
Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

```

 **Example 3:** 

```
Input: s = ")("
Output: [""]

```

 

 **Constraints:** 

- 1 <= s.length <= 25
- s consists of lowercase English letters and parentheses '(' and ')'.
- There will be at most 20 parentheses in s.

## Solution

**Language:** Python  
**Runtime:** 2795 ms (beats 5.25%)  
**Memory:** 12.6 MB (beats 75.93%)  
**Submitted:** 2026-10-07T16:34:07.479Z  

```py
class Solution(object):
    def removeInvalidParentheses(self, s):

        result = set()

        def dfs(i, path, balance, left_remove, right_remove):

            if i == len(s):
                if balance == 0 and left_remove == 0 and right_remove == 0:
                    result.add("".join(path))
                return

            ch = s[i]

            # Case 1: character is '('
            if ch == '(':

                # Remove it
                if left_remove > 0:
                    dfs(i + 1, path, balance,
                        left_remove - 1, right_remove)

                # Keep it
                path.append(ch)
                dfs(i + 1, path, balance + 1,
                    left_remove, right_remove)
                path.pop()

            # Case 2: character is ')'
            elif ch == ')':

                # Remove it
                if right_remove > 0:
                    dfs(i + 1, path, balance,
                        left_remove, right_remove - 1)

                # Keep it only if valid
                if balance > 0:
                    path.append(ch)
                    dfs(i + 1, path, balance - 1,
                        left_remove, right_remove)
                    path.pop()

            # Case 3: normal letter
            else:
                path.append(ch)
                dfs(i + 1, path, balance,
                    left_remove, right_remove)
                path.pop()

        # Count how many '(' and ')' must be removed
        left_remove = 0
        right_remove = 0

        for ch in s:
            if ch == '(':
                left_remove += 1

            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        dfs(0, [], 0, left_remove, right_remove)

        return list(result)
```

---

[View on LeetCode](https://leetcode.com/problems/remove-invalid-parentheses/)