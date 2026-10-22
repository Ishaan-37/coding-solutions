class Solution(object):
    def minOperations(self, A):
        n = len(A)
        asc, dsc = 1, 1
        for i in range(1, n):
            if A[i] == (A[i - 1] + 1) % n:
                asc += 1
            if A[i - 1] == (A[i] + 1) % n:
                dsc += 1
        if asc == n and A[0] == 0:
            return 0
        if asc == n:
            return min(n - A[0], A[0] + 2)
        if dsc == n:
            return min(n - A[-1], A[-1]) + 1
        return -1