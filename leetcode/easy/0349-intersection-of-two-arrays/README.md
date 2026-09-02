# Intersection of Two Arrays

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two integer arrays `nums1` and `nums2`, return  *an array of their intersection*. Each element in the result must be  **unique**  and you may return the result in  **any order**.

 

 **Example 1:** 

```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

```

 **Example 2:** 

```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

```

 

 **Constraints:** 

- 1 <= nums1.length, nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 1000

## Solution

**Language:** Python  
**Runtime:** 19 ms (beats 16.36%)  
**Memory:** 12.3 MB (beats 94.55%)  
**Submitted:** 2026-09-02T09:15:47.148Z  

```py
class Solution(object):
    def intersection(self, nums1, nums2):
        result = []
        for x in nums1:
            if x in nums2 and x not in result:
                result.append(x)
        return result
        
```

---

[View on LeetCode](https://leetcode.com/problems/intersection-of-two-arrays/)