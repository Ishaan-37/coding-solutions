# Number of Sub-arrays With Odd Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array of integers `arr`, return  *the number of subarrays with an  **odd**  sum*.

Since the answer can be very large, return it modulo `109 + 7`.

 

Original
Python3
 **Example 1:** 

```
Input: arr = [1,3,5]
Output: 4
Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.

```

 **Example 2:** 

```
Input: arr = [2,4,6]
Output: 0
Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.

```

 **Example 3:** 

```
Input: arr = [1,2,3,4,5,6,7]
Output: 16

```

 

 **Constraints:** 

- 1 <= arr.length <= 105
- 1 <= arr[i] <= 100

## Solution

**Language:** Python  
**Runtime:** 61 ms (beats 88.61%)  
**Memory:** 24.4 MB (beats 78.69%)  
**Submitted:** 2026-11-15T03:16:51.986Z  

```py
class Solution(object):
    def numOfSubarrays(self, arr):
        MOD = 10**9 + 7
        even, odd = 1, 0   # prefix sums seen so far (empty prefix = even)
        parity = 0
        res = 0
        for x in arr:
            parity = (parity + x) % 2
            if parity:          # odd prefix -> pair with earlier even prefixes
                res += even
                odd += 1
            else:               # even prefix -> pair with earlier odd prefixes
                res += odd
                even += 1
        return res % MOD
```

---

[View on LeetCode](https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/)