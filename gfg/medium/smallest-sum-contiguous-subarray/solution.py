class Solution:
    def minSubarraySum(self, arr: list[int]) -> int:
        # code here
        min_sum = arr[0]
        cur_sum = arr[0]
        for n in arr[1:]:
            cur_sum = min( n, cur_sum + n )
            min_sum = min( min_sum, cur_sum )
        return min_sum