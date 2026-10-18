class Solution(object):
    def numOfWays(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = dp[i][i] = 1
            for j in range(1, i):
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % MOD
        def solve(arr):
            if len(arr) <= 2:
                return 1
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            return (dp[len(left) + len(right)][len(left)]
                    * solve(left) * solve(right)) % MOD
        return (solve(nums) - 1) % MOD