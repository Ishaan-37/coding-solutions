
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:

        tree = [0] * (4 * k)

        def build(node, start, end):
            tree[node] = end - start + 1

            if start == end:
                return

            mid = (start + end) // 2
            build(node * 2, start, mid)
            build(node * 2 + 1, mid + 1, end)

        def update(node, start, end, idx, val):
            if start == end:
                tree[node] = val
                return

            mid = (start + end) // 2

            if idx <= mid:
                update(node * 2, start, mid, idx, val)
            else:
                update(node * 2 + 1, mid + 1, end, idx, val)

            tree[node] = tree[node * 2] + tree[node * 2 + 1]

        def find_first(node, start, end, left, right):
            if right < start or end < left or tree[node] == 0:
                return -1

            if start == end:
                return start

            mid = (start + end) // 2

            res = find_first(node * 2, start, mid, left, right)

            if res != -1:
                return res

            return find_first(node * 2 + 1, mid + 1, end, left, right)

        build(1, 0, k - 1)

        busy = []
        count = [0] * k

        for i in range(len(arrival)):

            # Release completed servers
            while busy and busy[0][0] <= arrival[i]:
                finish, server = heapq.heappop(busy)
                update(1, 0, k - 1, server, 1)

            target = i % k

            # Find server from target to k-1
            server = find_first(1, 0, k - 1, target, k - 1)

            # Wrap around if needed
            if server == -1:
                server = find_first(1, 0, k - 1, 0, target - 1)

            # All servers are busy
            if server == -1:
                continue

            # Mark server busy
            update(1, 0, k - 1, server, 0)

            count[server] += 1

            heapq.heappush(
                busy,
                (arrival[i] + load[i], server)
            )

        maximum = max(count)

        return [i for i in range(k) if count[i] == maximum]
