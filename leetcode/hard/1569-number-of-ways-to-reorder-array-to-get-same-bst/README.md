# Number of Ways to Reorder Array to Get Same BST

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given an array `nums` that represents a permutation of integers from `1` to `n`. We are going to construct a binary search tree (BST) by inserting the elements of `nums` in order into an initially empty BST. Find the number of different ways to reorder `nums` so that the constructed BST is identical to that formed from the original array `nums`.

- For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, and 3 as a right child. The array [2,3,1] also yields the same BST but [3,2,1] yields a different BST.

Return  *the number of ways to reorder*  `nums`  *such that the BST formed is identical to the original BST formed from*  `nums`.

Since the answer may be very large,  **return it modulo** `109 + 7`.

 

 **Example 1:** 

```
Input: nums = [2,1,3]
Output: 1
Explanation: We can reorder nums to be [2,3,1] which will yield the same BST. There are no other ways to reorder nums which will yield the same BST.

```

 **Example 2:** 

```
Input: nums = [3,4,5,1,2]
Output: 5
Explanation: The following 5 arrays will yield the same BST: 
[3,1,2,4,5]
[3,1,4,2,5]
[3,1,4,5,2]
[3,4,1,2,5]
[3,4,1,5,2]

```

 **Example 3:** 

```
Input: nums = [1,2,3]
Output: 0
Explanation: There are no other orderings of nums that will yield the same BST.

```

 

 **Constraints:** 

- 1 <= nums.length <= 1000
- 1 <= nums[i] <= nums.length
- All integers in nums are distinct.

## Solution

**Language:** Python  
**Runtime:** 1776 ms (beats 5.55%)  
**Memory:** 176.2 MB (beats 11.11%)  
**Submitted:** 2026-10-18T06:46:15.752Z  

```py
class Solution(object):
    def numOfWays(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = dp[i][i] = 1
            for j in range(1, i):
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % MOD
        def solve(arr):
            if len(arr) <= 2:
                return 1
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            return (dp[len(left) + len(right)][len(left)]
                    * solve(left) * solve(right)) % MOD
        return (solve(nums) - 1) % MOD
```

---

[View on LeetCode](https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/)