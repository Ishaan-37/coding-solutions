# Binary Search

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

 

 **Example 1:** 

```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

```

 **Example 2:** 

```
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

```

 

 **Constraints:** 

- 1 <= nums.length <= 104
- -104 < nums[i], target < 104
- All the integers in nums are unique.
- nums is sorted in ascending order.

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 12.4 MB  
**Submitted:** 2026-09-05T17:28:22.006Z  

```py
class Solution(object):
    def search(self, nums, target):
        low = 0 
        high = len(nums)-1
        while low <= high:
            guess = (low + high) // 2
            if nums[guess] == target:
                return guess
            elif nums[guess]< target:
                low = guess + 1
            else:
                high = guess - 1
        return -1
```

---

[View on LeetCode](https://leetcode.com/problems/binary-search/)