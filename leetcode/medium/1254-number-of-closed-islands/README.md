# Number of Closed Islands

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a 2D `grid` consists of `0s` (land) and `1s` (water).  An  *island*  is a maximal 4-directionally connected group of `0s` and a  *closed island*  is an island  **totally**  (all left, top, right, bottom) surrounded by `1s.`

Return the number of  *closed islands*.

 

 **Example 1:** 

```
Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
```

 **Example 2:** 

```
Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1

```

 **Example 3:** 

```
Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2

```

 

 **Constraints:** 

- 1 <= grid.length, grid[0].length <= 100
- 0 <= grid[i][j] <=1

## Solution

**Language:** Python  
**Runtime:** 22 ms (beats 71.77%)  
**Memory:** 12.4 MB (beats 93.55%)  
**Submitted:** 2026-10-25T05:07:39.820Z  

```py
class Solution(object):
    def closedIsland(self, grid):
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if grid[i][j] == 1:
                return True
            grid[i][j] = 1
            a = dfs(i + 1, j)
            b = dfs(i - 1, j)
            c = dfs(i, j + 1)
            d = dfs(i, j - 1)
            return a and b and c and d
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if dfs(i, j):
                        count += 1
        return count
```

---

[View on LeetCode](https://leetcode.com/problems/number-of-closed-islands/)