# Longest Substring Without Repeating Characters

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string `s`, find the length of the  **longest**   **substring**  without duplicate characters.

 

 **Example 1:** 

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

```

 **Example 2:** 

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

```

 **Example 3:** 

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

```

 

 **Constraints:** 

- 0 <= s.length <= 105
- s consists of English letters, digits, symbols and spaces.

## Solution

**Language:** Python  
**Runtime:** 379 ms (beats 15.96%)  
**Memory:** 16.5 MB (beats 6.65%)  
**Submitted:** 2026-08-05T11:09:12.100Z  

```py
class Solution(object):
    def lengthOfLongestSubstring(self, s):

        # Dictionary to store the frequency of characters
        char_count = {}

        # Left pointer of the sliding window
        left = 0

        # Stores the maximum length of a valid substring
        max_len = 0

        # Right pointer expands the window
        for right in range(len(s)):

            # Add the current character to the dictionary
            char_count[s[right]] = char_count.get(s[right], 0) + 1

            # If the current character is repeated,
            # shrink the window from the left
            while char_count[s[right]] > 1:

                # Remove the leftmost character
                char_count[s[left]] -= 1

                # Move the left pointer
                left += 1

            # Current window length
            current_len = right - left + 1

            # Update the maximum length
            if current_len > max_len:
                max_len = current_len

        # Return the answer
        return max_len
```

---

[View on LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)