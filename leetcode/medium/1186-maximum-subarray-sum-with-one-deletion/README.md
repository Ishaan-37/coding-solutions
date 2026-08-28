# Maximum Subarray Sum with One Deletion

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array of integers, return the maximum sum for a  **non-empty**  subarray (contiguous elements) with at most one element deletion. In other words, you want to choose a subarray and optionally delete one element from it so that there is still at least one element left and the sum of the remaining elements is maximum possible.

Note that the subarray needs to be  **non-empty**  after deleting one element.

 

 **Example 1:** 

```
Input: arr = [1,-2,0,3]
Output: 4
Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.
```

 **Example 2:** 

```
Input: arr = [1,-2,-2,3]
Output: 3
Explanation: We just choose [3] and it's the maximum sum.

```

 **Example 3:** 

```
Input: arr = [-1,-1,-1,-1]
Output: -1
Explanation: The final subarray needs to be non-empty. You can't choose [-1] and delete -1 from it, then get an empty subarray to make the sum equals to 0.

```

 

 **Constraints:** 

- 1 <= arr.length <= 105
- -104 <= arr[i] <= 104

## Solution

**Language:** Python  
**Runtime:** 35 ms (beats 97.67%)  
**Memory:** 17.5 MB (beats 87.55%)  
**Submitted:** 2026-08-28T20:44:50.014Z  

```py
class Solution(object):
    def maximumSum(self, arr):
        no_del = arr[0]
        one_del = -10**9
        ans = arr[0]

        for n in arr[1:]:
            old = no_del
            no_del = max(n, no_del + n)
            one_del = max(one_del + n, old)
            ans = max(ans, no_del, one_del)

        return ans
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/)