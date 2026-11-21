# Maximum Product Subarray

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums`, find a subarray that has the largest product, and return  *the product*.

The test cases are generated so that the answer will fit in a  **32-bit**  integer.

 **Note**  that the product of an array with a single element is the value of that element.

 

 **​​​​​​​Example 1:** 

```
Input:OriginalPython nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

```

 **Example 2:** 

```
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

```

 

 **Constraints:** 

- 1 <= nums.length <= 2 * 104
- -10 <= nums[i] <= 10
- The product of any subarray of nums is guaranteed to fit in a 32-bit integer.

## Solution

**Language:** Python  
**Runtime:** 8 ms (beats 82.08%)  
**Memory:** 12.7 MB (beats 78.82%)  
**Submitted:** 2026-11-21T06:21:22.668Z  

```py
class Solution(object):
    def maxProduct(self, nums):
        ans = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]
        for i in nums[1:]:
            if i < 0:
                curr_max, curr_min = curr_min, curr_max 
            curr_max = max(i, curr_max * i)
            curr_min = min(i, curr_min * i)
            ans = max(ans, curr_max)
        return ans               
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-product-subarray/)