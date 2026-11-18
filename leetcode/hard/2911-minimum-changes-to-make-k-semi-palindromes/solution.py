class Solution(object):
    def minimumChanges(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        
        # Precompute proper divisors for every possible substring length (2 to n)
        divisors = [[] for _ in range(n + 1)]
        for d in range(1, n):
            for length in range(2 * d, n + 1, d):
                divisors[length].append(d)
                
        # Precompute minimum changes to make substring s[i:j+1] a semi-palindrome
        INF = float('inf')
        cost = [[INF] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                min_changes = INF
                for d in divisors[length]:
                    changes = 0
                    # Check each of the d interleaved groups
                    for rem in range(d):
                        left = i + rem
                        right = j - (d - 1 - rem)
                        while left < right:
                            if s[left] != s[right]:
                                changes += 1
                            left += d
                            right -= d
                    if changes < min_changes:
                        min_changes = changes
                cost[i][j] = min_changes
                
        # DP[parts][end_idx]: min changes to partition s[0..end_idx] into `parts` substrings
        dp = [[INF] * n for _ in range(k + 1)]
        
        for j in range(1, n):
            dp[1][j] = cost[0][j]
            
        for parts in range(2, k + 1):
            # Minimum length for `parts` semi-palindromes is 2 * parts
            for j in range(2 * parts - 1, n):
                for prev_end in range(2 * (parts - 1) - 1, j - 1):
                    if dp[parts - 1][prev_end] != INF:
                        val = dp[parts - 1][prev_end] + cost[prev_end + 1][j]
                        if val < dp[parts][j]:
                            dp[parts][j] = val
                            
        return dp[k][n - 1]