# Subarrays Distinct Element Sum of Squares II

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given a  **0-indexed** integer array `nums`.

The  **distinct count**  of a subarray of `nums` is defined as:

- Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].

Return  *the sum of the  **squares**  of  **distinct counts**  of all subarrays of* `nums`.

Since the answer may be very large, return it  **modulo**  `109 + 7`.

A subarray is a contiguous  **non-empty**  sequence of elements within an array.

 

 **Example 1:** 

```
Input: nums = [1,2,1]
Output: 15
Explanation: Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 + 22 + 22 + 22 = 15.

```

 **Example 2:** 

```
Input: nums = [2,2]
Output: 3
Explanation: Three possible subarrays are:
[2]: 1 distinct value
[2]: 1 distinct value
[2,2]: 1 distinct value
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 = 3.
```

 

 **Constraints:** 

- 1 <= nums.length <= 105
- 1 <= nums[i] <= 105

## Solution

**Language:** Python  
**Runtime:** 6664 ms (beats 75.00%)  
**Memory:** 75.6 MB (beats 50.00%)  
**Submitted:** 2026-10-16T16:44:45.909Z  

```py
class Solution(object):
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        size = 4 * n
        sq = [0] * size
        sm = [0] * size
        lazy = [0] * size
        last = {}
        ans = 0

        def apply(node, length, v):
            sq[node] += 2 * v * sm[node] + v * v * length
            sm[node] += v * length
            lazy[node] += v

        def push(node, l, r):
            v = lazy[node]
            if v:
                m = (l + r) // 2
                apply(node * 2, m - l + 1, v)
                apply(node * 2 + 1, r - m, v)
                lazy[node] = 0

        def update(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                apply(node, r - l + 1, 1)
                return
            push(node, l, r)
            m = (l + r) // 2
            if ql <= m:
                update(node * 2, l, m, ql, qr)
            if qr > m:
                update(node * 2 + 1, m + 1, r, ql, qr)
            sq[node] = sq[node * 2] + sq[node * 2 + 1]
            sm[node] = sm[node * 2] + sm[node * 2 + 1]

        for i, x in enumerate(nums):
            p = last.get(x, -1)
            update(1, 0, n - 1, p + 1, i)
            last[x] = i
            ans = (ans + sq[1]) % MOD

        return ans
```

---

[View on LeetCode](https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/)