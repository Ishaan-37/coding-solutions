# Search Insert Position

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

 

 **Example 1:** 

```
Input: nums = [1,3,5,6], target = 5
Output: 2

```

 **Example 2:** 

```
Input: nums = [1,3,5,6], target = 2
Output: 1

```

 **Example 3:** 

```
Input: nums = [1,3,5,6], target = 7
Output: 4

```

 

 **Constraints:** 

- 1 <= nums.length <= 104
- -104 <= nums[i] <= 104
- nums contains distinct values sorted in ascending order.
- -104 <= target <= 104

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 4.18%)  
**Memory:** 12.8 MB (beats 95.30%)  
**Submitted:** 2026-09-07T10:25:54.970Z  

```py
class Solution(object):
    def searchInsert(self, nums, target):
        n = len(nums)
        ans = 0
        for i in range(n):
            if nums[i]>= target:
                return i
        return n
```

---

[View on LeetCode](https://leetcode.com/problems/search-insert-position/)