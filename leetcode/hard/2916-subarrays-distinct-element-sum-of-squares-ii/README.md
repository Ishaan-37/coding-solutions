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
**Runtime:** 6731 ms (beats 62.50%)  
**Memory:** 100 MB (beats 25.00%)  
**Submitted:** 2026-10-16T16:45:16.428Z  

```py
class Solution(object):
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        tree = [0] * (4 * n)
        lazy = [0] * (4 * n)
        sums = [0] * (4 * n)
        ans = 0
        last = {}
        def update(node, start, end, left, right):
            if left > end or right < start:
                return
            if left <= start and end <= right:
                length = end - start + 1
                tree[node] += 2 * sums[node] + length
                sums[node] += length
                lazy[node] += 1
                return
            mid = (start + end) // 2
            push(node, start, end, mid)
            update(node * 2, start, mid, left, right)
            update(node * 2 + 1, mid + 1, end, left, right)
            tree[node] = tree[node * 2] + tree[node * 2 + 1]
            sums[node] = sums[node * 2] + sums[node * 2 + 1]
        def push(node, start, end, mid):
            val = lazy[node]
            if val == 0:
                return
            for child, l, r in (
                (node * 2, start, mid),
                (node * 2 + 1, mid + 1, end)
            ):
                length = r - l + 1
                tree[child] += 2 * val * sums[child] + val * val * length
                sums[child] += val * length
                lazy[child] += val
            lazy[node] = 0
        for i, x in enumerate(nums):
            prev = last.get(x, -1)
            update(1, 0, n - 1, prev + 1, i)
            last[x] = i
            ans = (ans + tree[1]) % MOD
        return ans
```

---

[View on LeetCode](https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/)