# Minimum Size Subarray Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array of positive integers `nums` and a positive integer `target`, return  *the  **minimal length**  of a  **subarray**  whose sum is greater than or equal to*  `target`. If there is no such subarray, return `0` instead.

 

 **Example 1:** 

```
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

```

 **Example 2:** 

```
Input: target = 4, nums = [1,4,4]
Output: 1

```

 **Example 3:** 

```
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

```

 

 **Constraints:** 

- 1 <= target <= 109
- 1 <= nums.length <= 105
- 1 <= nums[i] <= 104

 

 **Follow up:**  If you have figured out the `O(n)` solution, try coding another solution of which the time complexity is `O(n log(n))`.

## Solution

**Language:** Python  
**Runtime:** 21 ms (beats 59.48%)  
**Memory:** 20.2 MB (beats 14.28%)  
**Submitted:** 2026-07-23T17:14:01.113Z  

```py
class Solution:
    def minSubArrayLen(self, target, nums):

        # Find the length of the array
        n = len(nums)

        # Left pointer of the sliding window
        left = 0

        # Stores the current window sum
        window_sum = 0

        # Initialize minimum length as infinity
        min_len = float('inf')

        # Expand the window by moving the right pointer
        for right in range(n):

            # Add the current element to the window sum
            window_sum += nums[right]

            # Shrink the window while the sum is
            # greater than or equal to the target
            while window_sum >= target:

                # Update the minimum length found so far
                min_len = min(min_len, right - left + 1)

                # Remove the leftmost element from the window
                window_sum -= nums[left]

                # Move the left pointer forward
                left += 1

        # If no valid subarray is found, return 0
        if min_len == float('inf'):
            return 0

        # Otherwise, return the minimum length
        return min_len
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-size-subarray-sum/)