# Third Maximum Number

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given an integer array `nums`.

Return the  **third distinct maximum**  number in this array. If the third  **maximum**  does not exist, return the  **maximum**  number.

 

 **Example 1:** 

```
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.

```

 **Example 2:** 

```
Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.

```

 **Example 3:** 

```
Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.

```

 

 **Constraints:** 

- 1 <= nums.length <= 104
- -231 <= nums[i] <= 231 - 1

 

 **Follow up:**  Can you find an `O(n)` solution?

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 13.2 MB (beats 19.64%)  
**Submitted:** 2026-09-01T20:14:01.294Z  

```py
class Solution(object):
    def thirdMax(self, nums):
        nums = list(set(nums)) #set(nums) duplicates hata deta hai: Lekin set ek set deta hai, list nahi.Isliye:list(set(nums)banega
        nums.sort(reverse=True) #reverse=True ka matlab:largest se smallest

        if len(nums) >= 3: #Ab check kar rahe hain:Kya kam se kam 3 distinct numbers hain?:len(nums) = list mein kitne elements hain.
            return nums[2] #Agar 3 ya usse zyada distinct numbers hain, toh third maximum return karo.
        else:
            return nums[0] #Third maximum exist na kare, toh maximum return karo.
        
        
```

---

[View on LeetCode](https://leetcode.com/problems/third-maximum-number/)