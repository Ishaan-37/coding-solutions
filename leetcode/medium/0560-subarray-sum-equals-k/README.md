# Subarray Sum Equals K

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array of integers `nums` and an integer `k`, return  *the total number of subarrays whose sum equals to*  `k`.

A subarray is a contiguous  **non-empty**  sequence of elements within an array.

 

 **Example 1:** 

```
Input: nums = [1,1,1], k = 2
Output: 2

```

 **Example 2:** 

```
Input: nums = [1,2,3], k = 3
Output: 2

```

 

 **Constraints:** 

- 1 <= nums.length <= 2 * 104
- -1000 <= nums[i] <= 1000
- -107 <= k <= 107

## Solution

**Language:** Python  
**Runtime:** 36 ms (beats 60.45%)  
**Memory:** 14.8 MB (beats 48.60%)  
**Submitted:** 2026-09-16T16:35:20.989Z  

```py
class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        total = 0
        d = {0: 1}
        for x in nums:
            total += x
            if total - k in d:
                count += d[total - k]
            d[total] = d.get(total, 0) + 1
        return count
```

---

[View on LeetCode](https://leetcode.com/problems/subarray-sum-equals-k/)