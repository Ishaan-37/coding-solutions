# Maximum Product Subarray

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums`, find a subarray that has the largest product, and return  *the product*.

The test cases are generated so that the answer will fit in a  **32-bit**  integer.

 **Note**  that the product of an array with a single element is the value of that element.

 

 **Example 1:** 

```
Input: nums = [2,3,-2,4]
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
**Runtime:** 7 ms (beats 93.52%)  
**Memory:** 12.7 MB (beats 93.86%)  
**Submitted:** 2026-08-28T19:58:40.778Z  

```py
class Solution(object):
    def maxProduct(self, nums):
        max_prod = nums[0] 
        cur_max = nums[0]
        cur_min = nums[0]
        for n in nums[1:]:
            candidates = ( n, cur_max*n, cur_min*n )
            cur_max, cur_min = max(candidates), min(candidates)
            max_prod = max(max_prod, cur_max)
        return max_prod
        
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-product-subarray/)