# Sort Colors

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array `nums` with `n` objects colored red, white, or blue, sort them  **in-place** so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

 **Example 1:** 

```
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

```

 **Example 2:** 

```
Input: nums = [2,0,1]
Output: [0,1,2]

```

 

 **Constraints:** 

- n == nums.length
- 1 <= n <= 300
- nums[i] is either 0, 1, or 2.

 

 **Follow up:**  Could you come up with a one-pass algorithm using only constant extra space?

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 12.6 MB (beats 17.68%)  
**Submitted:** 2026-07-16T09:51:40.337Z  

```py
class Solution:
    def sortColors(self, nums):

        # Count the number of 0s, 1s, and 2s
        count0 = 0
        count1 = 0
        count2 = 0

        # Traverse the array once to count each value
        for num in nums:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 += 1

        # Start filling the array from index 0
        index = 0

        # Fill all the 0s
        while count0 > 0:
            nums[index] = 0
            index += 1
            count0 -= 1

        # Fill all the 1s
        while count1 > 0:
            nums[index] = 1
            index += 1
            count1 -= 1

        # Fill all the 2s
        while count2 > 0:
            nums[index] = 2
            index += 1
            count2 -= 1
```

---

[View on LeetCode](https://leetcode.com/problems/sort-colors/)