# Minimum Operations to Make Elements Within K Subarrays Equal

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given an integer array `nums` and two integers, `x` and `k`. You can perform the following operation any number of times (**including zero**):

- Increase or decrease any element of nums by 1.

Return the  **minimum**  number of operations needed to have  **at least**  `k`  *non-overlapping subarrays*  of size  **exactly**  `x` in `nums`, where all elements within each subarray are equal.

 

 **Example 1:** 

 **Input:**  nums = [5,-2,1,3,7,3,6,4,-1], x = 3, k = 2

 **Output:**  8

 **Explanation:** 

- Use 3 operations to add 3 to nums[1] and use 2 operations to subtract 2 from nums[3]. The resulting array is [5, 1, 1, 1, 7, 3, 6, 4, -1].
- Use 1 operation to add 1 to nums[5] and use 2 operations to subtract 2 from nums[6]. The resulting array is [5, 1, 1, 1, 7, 4, 4, 4, -1].
- Now, all elements within each subarray [1, 1, 1] (from indices 1 to 3) and [4, 4, 4] (from indices 5 to 7) are equal. Since 8 total operations were used, 8 is the output.

 **Example 2:** 

 **Input:**  nums = [9,-2,-2,-2,1,5], x = 2, k = 2

 **Output:**  3

 **Explanation:** 

- Use 3 operations to subtract 3 from nums[4]. The resulting array is [9, -2, -2, -2, -2, 5].
- Now, all elements within each subarray [-2, -2] (from indices 1 to 2) and [-2, -2] (from indices 3 to 4) are equal. Since 3 operations were used, 3 is the output.

 

 **Constraints:** 

- 2 <= nums.length <= 105
- -106 <= nums[i] <= 106
- 2 <= x <= nums.length
- 1 <= k <= 15
- 2 <= k * x <= nums.length

## Solution

**Language:** Python  
**Runtime:** 7326 ms (beats 11.54%)  
**Memory:** 40.1 MB (beats 82.69%)  
**Submitted:** 2026-11-04T04:49:55.675Z  

```py
from bisect import bisect_left

class Solution:
    def minOperations(self, nums, x, k):
        n = len(nums)
        vals = sorted(set(nums))
        m = len(vals)

        def update(bit, i, v):
            while i <= m:
                bit[i] += v
                i += i & -i

        def query(bit, i):
            s = 0
            while i:
                s += bit[i]
                i -= i & -i
            return s

        def kth(bit, k):
            idx = 0
            step = 1 << (m.bit_length() - 1)

            while step:
                nxt = idx + step
                if nxt <= m and bit[nxt] < k:
                    idx = nxt
                    k -= bit[nxt]
                step >>= 1

            return vals[idx]

        cnt = [0] * (m + 1)
        sums = [0] * (m + 1)

        for i in range(x):
            p = bisect_left(vals, nums[i]) + 1
            update(cnt, p, 1)
            update(sums, p, nums[i])

        costs = []

        for i in range(n - x + 1):
            median = kth(cnt, (x + 1) // 2)
            p = bisect_left(vals, median) + 1

            c = query(cnt, p)
            s = query(sums, p)
            total = query(sums, m)

            cost = median * c - s + total - s - median * (x - c)
            costs.append(cost)

            if i + x < n:
                old = bisect_left(vals, nums[i]) + 1
                new = bisect_left(vals, nums[i + x]) + 1

                update(cnt, old, -1)
                update(sums, old, -nums[i])

                update(cnt, new, 1)
                update(sums, new, nums[i + x])

        INF = float('inf')
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(n - 1, -1, -1):
                curr[i] = curr[i + 1]

                if i + x <= n:
                    curr[i] = min(
                        curr[i],
                        costs[i] + prev[i + x]
                    )

            prev = curr

        return prev[0]
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/)