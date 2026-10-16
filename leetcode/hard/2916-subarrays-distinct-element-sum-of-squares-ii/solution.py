class Solution(object):
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        size = 4 * n
        sq = [0] * size
        sm = [0] * size
        lazy = [0] * size
        last = {}
        ans = 0

        def apply(node, length, v):
            sq[node] += 2 * v * sm[node] + v * v * length
            sm[node] += v * length
            lazy[node] += v

        def push(node, l, r):
            v = lazy[node]
            if v:
                m = (l + r) // 2
                apply(node * 2, m - l + 1, v)
                apply(node * 2 + 1, r - m, v)
                lazy[node] = 0

        def update(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                apply(node, r - l + 1, 1)
                return
            push(node, l, r)
            m = (l + r) // 2
            if ql <= m:
                update(node * 2, l, m, ql, qr)
            if qr > m:
                update(node * 2 + 1, m + 1, r, ql, qr)
            sq[node] = sq[node * 2] + sq[node * 2 + 1]
            sm[node] = sm[node * 2] + sm[node * 2 + 1]

        for i, x in enumerate(nums):
            p = last.get(x, -1)
            update(1, 0, n - 1, p + 1, i)
            last[x] = i
            ans = (ans + sq[1]) % MOD

        return ans