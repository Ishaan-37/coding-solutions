class Solution(object):
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        tree = [0] * (4 * n)
        lazy = [0] * (4 * n)
        sums = [0] * (4 * n)
        ans = 0
        last = {}
        def update(node, start, end, left, right):
            if left > end or right < start:
                return
            if left <= start and end <= right:
                length = end - start + 1
                tree[node] += 2 * sums[node] + length
                sums[node] += length
                lazy[node] += 1
                return
            mid = (start + end) // 2
            push(node, start, end, mid)
            update(node * 2, start, mid, left, right)
            update(node * 2 + 1, mid + 1, end, left, right)
            tree[node] = tree[node * 2] + tree[node * 2 + 1]
            sums[node] = sums[node * 2] + sums[node * 2 + 1]
        def push(node, start, end, mid):
            val = lazy[node]
            if val == 0:
                return
            for child, l, r in (
                (node * 2, start, mid),
                (node * 2 + 1, mid + 1, end)
            ):
                length = r - l + 1
                tree[child] += 2 * val * sums[child] + val * val * length
                sums[child] += val * length
                lazy[child] += val
            lazy[node] = 0
        for i, x in enumerate(nums):
            prev = last.get(x, -1)
            update(1, 0, n - 1, prev + 1, i)
            last[x] = i
            ans = (ans + tree[1]) % MOD
        return ans