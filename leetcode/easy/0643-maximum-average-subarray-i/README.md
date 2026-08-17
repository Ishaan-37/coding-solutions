# Maximum Average Subarray I

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given an integer array `nums` consisting of `n` elements, and an integer `k`.

Find a contiguous subarray whose  **length is equal to**  `k` that has the maximum average value and return  *this value*. Any answer with a calculation error less than `10-5` will be accepted.

 

 **Example 1:** 

```
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

```

 **Example 2:** 

```
Input: nums = [5], k = 1
Output: 5.00000

```

 

 **Constraints:** 

- n == nums.length
- 1 <= k <= n <= 105
- -104 <= nums[i] <= 104

## Solution

**Language:** Python  
**Runtime:** 122 ms (beats 19.05%)  
**Memory:** 18.9 MB (beats 80.43%)  
**Submitted:** 2026-08-17T17:21:40.371Z  

```py
class Solution(object):
    def findMaxAverage(self, nums, k):
        left = 0
        window_sum = 0
        ans = float("-inf")
        for right in range(len(nums)):
            window_sum += nums[right]
            if right - left + 1 == k:
                ans = max(ans,window_sum)
                window_sum -= nums[left]
                left +=1
        return ans / float(k) 


        
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-average-subarray-i/)