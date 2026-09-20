# Permutations

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in  **any order**.

 

 **Example 1:** 

```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

```

 **Example 2:** 

```
Input: nums = [0,1]
Output: [[0,1],[1,0]]

```

 **Example 3:** 

```
Input: nums = [1]
Output: [[1]]

```

 

 **Constraints:** 

- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- All the integers of nums are unique.

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 55.76%)  
**Memory:** 12.6 MB (beats 57.61%)  
**Submitted:** 2026-09-20T09:21:06.383Z  

```py
class Solution(object):
    def permute(self, nums):
        result = []
        current = []
        def backtrack():
            if len(current) == len(nums):
                result.append(current[:])
                return
            for i in range(len(nums)):
                if nums[i] not in current:
                    current.append(nums[i])
                    backtrack()
                    current.pop()
        backtrack()
        return result
```

---

[View on LeetCode](https://leetcode.com/problems/permutations/)