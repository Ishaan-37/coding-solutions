class Solution(object):
    def minMoves(self, nums):
        max_num = max(nums)
        moves = 0

        for num in nums:
            moves += max_num - num

        return moves