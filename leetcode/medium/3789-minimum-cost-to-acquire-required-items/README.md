# Minimum Cost to Acquire Required Items

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given five integers `cost1`, `cost2`, `costBoth`, `need1`, and `need2`.

There are three types of items available:

- An item of type 1 costs cost1 and contributes 1 unit to the type 1 requirement only.
- An item of type 2 costs cost2 and contributes 1 unit to the type 2 requirement only.
- An item of type 3 costs costBoth and contributes 1 unit to both type 1 and type 2 requirements.

You must collect enough items so that the total contribution toward type 1 is  **at least**  `need1` and the total contribution toward type 2 is  **at least**  `need2`.

Return an integer representing the  **minimum**  possible total cost to achieve these requirements.

 

Original
Python
 **Example 1:** 

 **Input:**  cost1 = 3, cost2 = 2, costBoth = 1, need1 = 3, need2 = 2

 **Output:**  3

 **Explanation:** 

After buying three type 3 items, which cost `3 * 1 = 3`, the total contribution to type 1 is 3 (`>= need1 = 3`) and to type 2 is 3 (`>= need2 = 2`).
Any other valid combination would cost more, so the minimum total cost is 3.

 **Example 2:** 

 **Input:**  cost1 = 5, cost2 = 4, costBoth = 15, need1 = 2, need2 = 3

 **Output:**  22

 **Explanation:** 

We buy `need1 = 2` items of type 1 and `need2 = 3` items of type 2: `2  *5 + 3*  4 = 10 + 12 = 22`.
Any other valid combination would cost more, so the minimum total cost is 22.

 **Example 3:** 

 **Input:**  cost1 = 5, cost2 = 4, costBoth = 15, need1 = 0, need2 = 0

 **Output:**  0

 **Explanation:** 

Since no items are required (`need1 = need2 = 0`), we buy nothing and pay 0.

 

 **Constraints:** 

- 1 <= cost1, cost2, costBoth <= 106
- 0 <= need1, need2 <= 109

## Solution

**Language:** Python  
**Runtime:** 1 ms (beats 58.33%)  
**Memory:** 12.2 MB (beats 75.00%)  
**Submitted:** 2026-11-11T07:03:23.041Z  

```py
class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):

        ans1 = need1 * cost1 + need2 * cost2

        ans2 = max(need1, need2) * costBoth

        ans3 = min(need1, need2) * costBoth

        if need1 > need2:
            ans3 += (need1 - need2) * cost1
        else:
            ans3 += (need2 - need1) * cost2

        return min(ans1, ans2, ans3)
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-cost-to-acquire-required-items/)