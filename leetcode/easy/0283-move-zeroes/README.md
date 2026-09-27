# Move Zeroes

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

 **Note**  that you must do this in-place without making a copy of the array.

 

 **Example 1:** 

```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

```

 **Example 2:** 

```
Input: nums = [0]
Output: [0]

```

 

 **Constraints:** 

- 1 <= nums.length <= 104
- -231 <= nums[i] <= 231 - 1

 

 **Follow up:**  Could you minimize the total number of operations done?

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 12.4 MB  
**Submitted:** 2026-09-27T17:01:59.657Z  

```py
class Solution:
    def moveZeroes(self, nums):
        j = 0 # Pointer to place the next non-zero element
        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap current element with the element at index j 
                nums[i], nums[j] = nums[j], nums[i]
                j += 1 # Move j to the next index for placing non-zero
            


```

---

[View on LeetCode](https://leetcode.com/problems/move-zeroes/)