class Solution(object):
    def maximumSum(self, arr):
        no_del = arr[0]
        one_del = -10**9
        ans = arr[0]

        for n in arr[1:]:
            old = no_del
            no_del = max(n, no_del + n)
            one_del = max(one_del + n, old)
            ans = max(ans, no_del, one_del)

        return ans