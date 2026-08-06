# Longest Repeating Character Replacement

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return  *the length of the longest substring containing the same letter you can get after performing the above operations*.

 

 **Example 1:** 

```
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

```

 **Example 2:** 

```
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
```

 

 **Constraints:** 

- 1 <= s.length <= 105
- s consists of only uppercase English letters.
- 0 <= k <= s.length

## Solution

**Language:** Python  
**Runtime:** 83 ms (beats 99.21%)  
**Memory:** 15.5 MB (beats 29.15%)  
**Submitted:** 2026-08-06T08:45:39.425Z  

```py
class Solution(object):
    def characterReplacement(self, s, k):

        # Left pointer
        left = 0

        # Frequency dictionary
        freq = {}

        # Highest frequency inside current window
        max_freq = 0

        # Final answer
        ans = 0

        # Expand window
        for right in range(len(s)):

            # Current character
            ch = s[right]

            # Increase frequency
            freq[ch] = freq.get(ch, 0) + 1

            # Update maximum frequency
            if freq[ch] > max_freq:
                max_freq = freq[ch]

            # Current window size
            window = right - left + 1

            # If more than k replacements are needed
            while window - max_freq > k:

                # Remove left character
                freq[s[left]] -= 1

                # Move left pointer
                left += 1

                # Update window size
                window = right - left + 1

            # Update answer
            if window > ans:
                ans = window

        return ans
```

---

[View on LeetCode](https://leetcode.com/problems/longest-repeating-character-replacement/)