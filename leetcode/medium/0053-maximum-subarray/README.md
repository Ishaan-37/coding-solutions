# Maximum Subarray

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums`, find the subarray with the largest sum, and return  *its sum*.

 

 **Example 1:** 

```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

```

 **Example 2:** 

```
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

```

 **Example 3:** 

```
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

```

 

 **Constraints:** 

- 1 <= nums.length <= 105
- -104 <= nums[i] <= 104

 

 **Follow up:**  If you have figured out the `O(n)` solution, try coding another solution using the  **divide and conquer**  approach, which is more subtle.

## Solution

**Language:** Python  
**Runtime:** 92 ms (beats 53.78%)  
**Memory:** 20.9 MB (beats 95.05%)  
**Submitted:** 2026-08-28T19:44:33.213Z  

```py
class Solution(object):
    def maxSubArray(self, nums):
        max_sum = nums[0]
        cur_sum = nums[0]
        for n in nums[1:]:
            cur_sum = max( n, cur_sum + n )
            max_sum = max( max_sum, cur_sum )
        return max_sum
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-subarray/)