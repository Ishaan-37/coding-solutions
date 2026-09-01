# Top K Frequent Elements

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums` and an integer `k`, return  *the*  `k`  *most frequent elements*. You may return the answer in  **any order**.

 

 **Example 1:** 

 **Input:**  nums = [1,1,1,2,2,3], k = 2

 **Output:**  [1,2]

 **Example 2:** 

 **Input:**  nums = [1], k = 1

 **Output:**  [1]

 **Example 3:** 

 **Input:**  nums = [1,2,1,2,1,2,3,1,3,2], k = 2

 **Output:**  [1,2]

 

 **Constraints:** 

- 1 <= nums.length <= 105
- -104 <= nums[i] <= 104
- k is in the range [1, the number of unique elements in the array].
- It is guaranteed that the answer is unique.

 

 **Follow up:**  Your algorithm's time complexity must be better than `O(n log n)`, where n is the array's size.

## Solution

**Language:** Python  
**Runtime:** 6 ms (beats 84.65%)  
**Memory:** 14 MB (beats 96.88%)  
**Submitted:** 2026-09-01T16:10:28.737Z  

```py
class Solution(object):
    def topKFrequent(self, nums, k):
        d = {}
        for num in nums:
            d[num] = d.get(num,0)+1
        return sorted(d, key=d.get, reverse=True)[:k]
        
```

---

[View on LeetCode](https://leetcode.com/problems/top-k-frequent-elements/)