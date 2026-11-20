from collections import defaultdict


class Solution(object):

  def maxSelectedElements(self, nums):
    """
        :type nums: List[int]
        :rtype: int
        """
    nums.sort()
    # dp[v] stores the max length of a consecutive sequence ending at value v
    dp = defaultdict(int)

    for x in nums:
      # Update x + 1 first so we don't reuse the same element x twice
      dp[x + 1] = max(dp[x + 1], dp[x] + 1)
      dp[x] = max(dp[x], dp[x - 1] + 1)

    return max(dp.values())