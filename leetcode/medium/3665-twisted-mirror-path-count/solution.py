
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
