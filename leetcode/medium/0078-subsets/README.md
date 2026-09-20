# Subsets

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums` of  **unique**  elements, return  *all possible*   *subsets*   *(the power set)*.

The solution set  **must not**  contain duplicate subsets. Return the solution in  **any order**.

 

 **Example 1:** 

```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

```

 **Example 2:** 

```
Input: nums = [0]
Output: [[],[0]]

```

 

 **Constraints:** 

- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of nums are unique.

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 12.4 MB (beats 98.53%)  
**Submitted:** 2026-09-20T07:08:28.105Z  

```py
class Solution(object):
    def subsets(self, nums):
        result = []
        current = []
        def backtrack(i):
            if i == len(nums):                   # Base case
                result.append(current[:])  #Jo subset abhi bana,uski copy answer mein save karo.
                return
            backtrack(i + 1)  # Choice 1: DON'T take nums[i]
            current.append(nums[i])     # Choice 2: TAKE nums[i]
            backtrack(i + 1)           
            current.pop()    # Backtrack
        backtrack(0)
        return result
```

---

[View on LeetCode](https://leetcode.com/problems/subsets/)