# Twisted Mirror Path Count

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an `m x n` binary grid `grid` where:

- grid[i][j] == 0 represents an empty cell, and
- grid[i][j] == 1 represents a mirror.

A robot starts at the top-left corner of the grid `(0, 0)` and wants to reach the bottom-right corner `(m - 1, n - 1)`. It can move only  **right**  or  **down**. If the robot attempts to move into a mirror cell, it is  **reflected**  before entering that cell:

- If it tries to move right into a mirror, it is turned down and moved into the cell directly below the mirror.
- If it tries to move down into a mirror, it is turned right and moved into the cell directly to the right of the mirror.

If this reflection would cause the robot to move outside the `grid` boundaries, the path is considered invalid and should not be counted.

Return the number of unique valid paths from `(0, 0)` to `(m - 1, n - 1)`.

Since the answer may be very large, return it  **modulo**  `109 + 7`.

 **Note** : If a reflection moves the robot into a mirror cell, the robot is immediately reflected again based on the direction it used to enter that mirror: if it entered while moving right, it will be turned down; if it entered while moving down, it will be turned right. This process will continue until either the last cell is reached, the robot moves out of bounds or the robot moves to a non-mirror cell.

 

 **Example 1:** 

 **Input:**  grid = [[0,1,0],[0,0,1],[1,0,0]]

 **Output:**  5

 **Explanation:** 

Number	Full Path
1	(0, 0) → (0, 1) [M] → (1, 1) → (1, 2) [M] → (2, 2)
2	(0, 0) → (0, 1) [M] → (1, 1) → (2, 1) → (2, 2)
3	(0, 0) → (1, 0) → (1, 1) → (1, 2) [M] → (2, 2)
4	(0, 0) → (1, 0) → (1, 1) → (2, 1) → (2, 2)
5	(0, 0) → (1, 0) → (2, 0) [M] → (2, 1) → (2, 2)
- [M] indicates the robot attempted to enter a mirror cell and instead reflected.

 **Example 2:** 

 **Input:**  grid = [[0,0],[0,0]]

 **Output:**  2

 **Explanation:** 

Number	Full Path
1	(0, 0) → (0, 1) → (1, 1)
2	(0, 0) → (1, 0) → (1, 1)

 **Example 3:** 

 **Input:**  grid = [[0,1,1],[1,1,0]]

 **Output:**  1

 **Explanation:** 

Number	Full Path
1	(0, 0) → (0, 1) [M] → (1, 1) [M] → (1, 2)
`(0, 0) → (1, 0) [M] → (1, 1) [M] → (2, 1)` goes out of bounds, so it is invalid.

 

 **Constraints:** 

- m == grid.length
- n == grid[i].length
- 2 <= m, n <= 500
- grid[i][j] is either 0 or 1.
- grid[0][0] == grid[m - 1][n - 1] == 0

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.1 MB  
**Submitted:** 2026-11-01T06:58:31.466Z  

```py

class Solution:
    def uniquePaths(self, grid):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        R = [[-1] * n for _ in range(m)]
        D = [[-1] * n for _ in range(m)]

        # Precompute mirror reflections
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if grid[i][j] == 0:
                    continue

                # Entered mirror while moving RIGHT
                # Reflection sends robot DOWN
                x, y = i + 1, j

                if x < m:
                    if grid[x][y] == 0:
                        R[i][j] = x * n + y
                    else:
                        R[i][j] = D[x][y]

                # Entered mirror while moving DOWN
                # Reflection sends robot RIGHT
                x, y = i, j + 1

                if y < n:
                    if grid[x][y] == 0:
                        D[i][j] = x * n + y
                    else:
                        D[i][j] = R[x][y]

        # Dynamic Programming
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):

                if dp[i][j] == 0:
                    continue

                ways = dp[i][j]

                # Move RIGHT
                if j + 1 < n:
                    if grid[i][j + 1] == 0:
                        target = (i, j + 1)
                        dp[target[0]][target[1]] = (
                            dp[target[0]][target[1]] + ways
                        ) % MOD
                    else:
                        pos = R[i][j + 1]
                        if pos != -1:
                            x, y = pos // n, pos % n
                            dp[x][y] = (dp[x][y] + ways) % MOD

                # Move DOWN
                if i + 1 < m:
                    if grid[i + 1][j] == 0:
                        dp[i + 1][j] = (
                            dp[i + 1][j] + ways
                        ) % MOD
                    else:
                        pos = D[i + 1][j]
                        if pos != -1:
                            x, y = pos // n, pos % n
                            dp[x][y] = (dp[x][y] + ways) % MOD

        return dp[m - 1][n - 1]

```

---

[View on LeetCode](https://leetcode.com/problems/twisted-mirror-path-count/)