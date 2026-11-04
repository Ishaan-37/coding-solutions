from bisect import bisect_left

class Solution:
    def minOperations(self, nums, x, k):
        n = len(nums)
        vals = sorted(set(nums))
        m = len(vals)

        def update(bit, i, v):
            while i <= m:
                bit[i] += v
                i += i & -i

        def query(bit, i):
            s = 0
            while i:
                s += bit[i]
                i -= i & -i
            return s

        def kth(bit, k):
            idx = 0
            step = 1 << (m.bit_length() - 1)

            while step:
                nxt = idx + step
                if nxt <= m and bit[nxt] < k:
                    idx = nxt
                    k -= bit[nxt]
                step >>= 1

            return vals[idx]

        cnt = [0] * (m + 1)
        sums = [0] * (m + 1)

        for i in range(x):
            p = bisect_left(vals, nums[i]) + 1
            update(cnt, p, 1)
            update(sums, p, nums[i])

        costs = []

        for i in range(n - x + 1):
            median = kth(cnt, (x + 1) // 2)
            p = bisect_left(vals, median) + 1

            c = query(cnt, p)
            s = query(sums, p)
            total = query(sums, m)

            cost = median * c - s + total - s - median * (x - c)
            costs.append(cost)

            if i + x < n:
                old = bisect_left(vals, nums[i]) + 1
                new = bisect_left(vals, nums[i + x]) + 1

                update(cnt, old, -1)
                update(sums, old, -nums[i])

                update(cnt, new, 1)
                update(sums, new, nums[i + x])

        INF = float('inf')
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(n - 1, -1, -1):
                curr[i] = curr[i + 1]

                if i + x <= n:
                    curr[i] = min(
                        curr[i],
                        costs[i] + prev[i + x]
                    )

            prev = curr

        return prev[0]