# Count Servers that Communicate

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a map of a server center, represented as a `m * n` integer matrix `grid`, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

 

 **Example 1:** 

```
Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.
```

 **Example 2:** 

```
Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.

```

 **Example 3:** 

```
Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.

```

 

 **Constraints:** 

- m == grid.length
- n == grid[i].length
- 1 <= m <= 250
- 1 <= n <= 250
- grid[i][j] == 0 or 1

## Solution

**Language:** Python  
**Runtime:** 16 ms (beats 68.36%)  
**Memory:** 21.7 MB (beats 24.86%)  
**Submitted:** 2026-11-08T05:03:18.166Z  

```py

class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        rows = [0] * m
        cols = [0] * n

        # Count servers in each row and column
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1

        ans = 0

        # Count communicating servers
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if rows[i] > 1 or cols[j] > 1:
                        ans += 1

        return ans

```

---

[View on LeetCode](https://leetcode.com/problems/count-servers-that-communicate/)