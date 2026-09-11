# Majority Element II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array of size `n`, find all elements that appear more than `⌊n / 3⌋` times.

 

 **Example 1:** 

```
Input: nums = [3,2,3]
Output: [3]

```

 **Example 2:** 

```
Input: nums = [1]
Output: [1]

```

 **Example 3:** 

```
Input: nums = [1,2]
Output: [1,2]

```

 

 **Constraints:** 

- 1 <= nums.length <= 5 * 104
- -109 <= nums[i] <= 109

 

 **Follow up:**  Could you solve the problem in linear time and in `O(1)` space?

## Solution

**Language:** Python  
**Runtime:** 4 ms (beats 95.13%)  
**Memory:** 15.1 MB (beats 39.77%)  
**Submitted:** 2026-09-11T06:43:10.757Z  

```py
class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        d = {}
        ans = []
        for ch in nums:
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] = d[ch]+1
        for ch in d:
            if d[ch] > n//3 :
                ans.append(ch)
        return ans
```

---

[View on LeetCode](https://leetcode.com/problems/majority-element-ii/)