# Isomorphic Strings

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two strings `s` and `t`,  *determine if they are isomorphic*.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

 **Example 1:** 

 **Input:**  s = "egg", t = "add"

 **Output:**  true

 **Explanation:** 

The strings `s` and `t` can be made identical by:

- Mapping 'e' to 'a'.
- Mapping 'g' to 'd'.

 **Example 2:** 

 **Input:**  s = "f11", t = "b23"

 **Output:**  false

 **Explanation:** 

The strings `s` and `t` can not be made identical as `'1'` needs to be mapped to both `'2'` and `'3'`.

 **Example 3:** 

 **Input:**  s = "paper", t = "title"

 **Output:**  true

 

 **Constraints:** 

- 1 <= s.length <= 5 * 104
- t.length == s.length
- s and t consist of any valid ascii character.

## Solution

**Language:** Python  
**Runtime:** 9 ms (beats 65.41%)  
**Memory:** 13.4 MB (beats 82.65%)  
**Submitted:** 2026-09-17T10:24:30.295Z  

```py
class Solution(object):
    def isIsomorphic(self, s, t):
        map = {}          # stores: character from s -> character from t
        have = set()      # stores characters from t that are already used
        for i in range(len(s)):    # traverse both strings using the same index
            if s[i] in map:        # has this character from s been mapped before?
                if map[s[i]] != t[i]:   # existing mapping is different
                    return False        # example: o -> a already, but now o -> r
            else:                 # s[i] has no mapping yet
                if t[i] in have:  # is this t character already used by another s character?
                    return False  # example: a -> c and b -> c
                map[s[i]] = t[i]  # create the mapping
                have.add(t[i])    # remember that this t character is now used
        return True               # all characters followed the rules
```

---

[View on LeetCode](https://leetcode.com/problems/isomorphic-strings/)