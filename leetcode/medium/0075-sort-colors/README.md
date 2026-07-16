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
**Memory:** 12.3 MB (beats 54.76%)  
**Submitted:** 2026-07-16T10:41:21.775Z  

```py
class Solution:
    def sortColors(self, nums):

        # Pointer for placing 0s
        low = 0

        # Current element being checked
        mid = 0

        # Pointer for placing 2s
        high = len(nums) - 1

        # Traverse until all elements are processed
        while mid <= high:

            # If current element is 0
            if nums[mid] == 0:

                # Swap with low pointer
                nums[low], nums[mid] = nums[mid], nums[low]

                # Move both pointers forward
                low += 1
                mid += 1

            # If current element is 1
            elif nums[mid] == 1:

                # Already in correct position
                mid += 1

            # If current element is 2
            else:

                # Swap with high pointer
                nums[mid], nums[high] = nums[high], nums[mid]

                # Move high pointer backward
                high -= 1

                # Do NOT increment mid
                # The swapped element needs to be checked
```

---

[View on LeetCode](https://leetcode.com/problems/sort-colors/)