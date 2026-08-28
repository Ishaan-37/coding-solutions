# Minimum Sum Subarray

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array  **arr[]**, find the sub-array containing at least one number which has the minimum sum and return its sum.

 **Examples :** 

```
Input: arr[] = [3,-4, 2,-3,-1, 7,-5]
Output: -6
Explanation: The subarray is [-4,2,-3,-1] = -6
```

```
Input: arr[] = [2, 6, 8, 1, 4]
Output: 1
Explanation: The subarray is [1] = 1
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-28T19:51:55.601Z  

```py
class Solution:
    def minSubarraySum(self, arr: list[int]) -> int:
        # code here
        min_sum = arr[0]
        cur_sum = arr[0]
        for n in arr[1:]:
            cur_sum = min( n, cur_sum + n )
            min_sum = min( min_sum, cur_sum )
        return min_sum
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/smallest-sum-contiguous-subarray/1)