# Peak Index in a Mountain Array

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an integer  **mountain**  array `arr` of length `n` where the values increase to a  **peak element**  and then decrease.

Return the index of the peak element.

Your task is to solve it in `O(log(n))` time complexity.

 

 **Example 1:** 

 **Input:**  arr = [0,1,0]

 **Output:**  1

 **Example 2:** 

 **Input:**  arr = [0,2,1,0]

 **Output:**  1

 **Example 3:** 

 **Input:**  arr = [0,10,5,2]

 **Output:**  1

 

 **Constraints:** 

- 3 <= arr.length <= 105
- 0 <= arr[i] <= 106
- arr is guaranteed to be a mountain array.

## Solution

**Language:** Python  
**Runtime:** 15 ms (beats 9.64%)  
**Memory:** 21.3 MB (beats 94.87%)  
**Submitted:** 2026-09-13T13:08:45.869Z  

```py
class Solution(object):
    def peakIndexInMountainArray(self, arr):
        n = len(arr)
        for i in range(n):
            return arr.index(max(arr))
```

---

[View on LeetCode](https://leetcode.com/problems/peak-index-in-a-mountain-array/)