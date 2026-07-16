# 3Sum Closest

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums` of length `n` and an integer `target`, find three integers at  **distinct indices**  in `nums` such that the sum is closest to `target`.

Return  *the sum of the three integers*.

You may assume that each input would have exactly one solution.

 

 **Example 1:** 

```
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

```

 **Example 2:** 

```
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

```

 

 **Constraints:** 

- 3 <= nums.length <= 500
- -1000 <= nums[i] <= 1000
- -104 <= target <= 104

## Solution

**Language:** Python  
**Runtime:** 407 ms (beats 93.69%)  
**Memory:** 12.4 MB (beats 77.37%)  
**Submitted:** 2026-07-16T09:00:08.053Z  

```py
class Solution:
    def threeSumClosest(self, nums, target):

        nums.sort()
        n = len(nums)

        diff = float('inf')
        res_sum = 0

        for i in range(n - 2):

            left = i + 1
            right = n - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]
                d = abs(target - total)

                if d < diff:
                    diff = d
                    res_sum = total

                if total == target:
                    return res_sum

                if total < target:
                    left += 1
                else:
                    right -= 1

        return res_sum
```

---

[View on LeetCode](https://leetcode.com/problems/3sum-closest/)