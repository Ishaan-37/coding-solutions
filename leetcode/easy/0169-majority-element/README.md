# Majority Element

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an array `nums` of size `n`, return  *the majority element*.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

 

 **Example 1:** 

```
Input: nums = [3,2,3]
Output: 3

```

 **Example 2:** 

```
Input: nums = [2,2,1,1,1,2,2]
Output: 2

```

 

 **Constraints:** 

- n == nums.length
- 1 <= n <= 5 * 104
- -109 <= nums[i] <= 109
- The input is generated such that a majority element will exist in the array.

 

 **Follow-up:**  Could you solve the problem in linear time and in `O(1)` space?

## Solution

**Language:** Python  
**Runtime:** 5 ms (beats 75.12%)  
**Memory:** 13.6 MB (beats 39.77%)  
**Submitted:** 2026-09-02T09:38:38.256Z  

```py
class Solution(object):
    def majorityElement(self, nums):
        return max(set(nums), key=nums.count)
```

---

[View on LeetCode](https://leetcode.com/problems/majority-element/)