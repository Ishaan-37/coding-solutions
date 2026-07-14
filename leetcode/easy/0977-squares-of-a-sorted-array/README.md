# Squares of a Sorted Array

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer array `nums` sorted in  **non-decreasing**  order, return  *an array of  **the squares of each number**  sorted in non-decreasing order*.

 

 **Example 1:** 

```
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

```

 **Example 2:** 

```
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

```

 

 **Constraints:** 

- 1 <= nums.length <= 104
- -104 <= nums[i] <= 104
- nums is sorted in non-decreasing order.

 

 **Follow up:**  Squaring each element and sorting the new array is very trivial, could you find an `O(n)` solution using a different approach?

## Solution

**Language:** Python  
**Runtime:** 20 ms (beats 13.13%)  
**Memory:** 14.2 MB (beats 44.37%)  
**Submitted:** 2026-07-14T09:27:48.363Z  

```py
class Solution:
    def sortedSquares(self, nums):

        negative = []
        positive = []

        # Separate negative and positive numbers
        for num in nums:
            if num < 0:
                negative.append(num)
            else:
                positive.append(num)

        # If there are no negative numbers
        if len(negative) == 0:
            return [x * x for x in positive]

        # If there are no positive numbers
        if len(positive) == 0:
            result = [x * x for x in negative]
            result.reverse()
            return result

        # Square the negative numbers and reverse them
        negative = [x * x for x in negative][::-1]

        # Square the positive numbers
        positive = [x * x for x in positive]

        # Store the sizes of both arrays
        n = len(negative)
        m = len(positive)

        # Store the final sorted squares
        result = []

        # Initialize two pointers
        i = 0
        j = 0

        # Merge the two sorted arrays
        while i < n and j < m:
            if negative[i] <= positive[j]:
                result.append(negative[i])
                i += 1
            else:
                result.append(positive[j])
                j += 1

        # Add remaining elements from negative array
        while i < n:
            result.append(negative[i])
            i += 1

        # Add remaining elements from positive array
        while j < m:
            result.append(positive[j])
            j += 1

        # Return the sorted squares
        return result
```

---

[View on LeetCode](https://leetcode.com/problems/squares-of-a-sorted-array/)