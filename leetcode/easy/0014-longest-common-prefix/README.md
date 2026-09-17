# Longest Common Prefix

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

 

 **Example 1:** 

```
Input: strs = ["flower","flow","flight"]
Output: "fl"

```

 **Example 2:** 

```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

```

 

 **Constraints:** 

- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lowercase English letters if it is non-empty.

## Solution

**Language:** Python  
**Runtime:** 4 ms (beats 14.90%)  
**Memory:** 12.5 MB (beats 35.31%)  
**Submitted:** 2026-09-17T16:06:47.502Z  

```py
class Solution(object):
    def longestCommonPrefix(self, strs):
        for i in range(len(strs[0])):
            for j in range(1 , len(strs)):
                if  i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                    return strs[0][:i]
        return strs[0]
```

---

[View on LeetCode](https://leetcode.com/problems/longest-common-prefix/)