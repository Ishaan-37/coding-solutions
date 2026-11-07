import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:

        available = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        ans = []
        current_time = 0

        for i, task in enumerate(tasks):

            current_time = max(current_time, i)

            while busy and busy[0][0] <= current_time:
                free_time, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            if not available:
                current_time = busy[0][0]

                while busy and busy[0][0] <= current_time:
                    free_time, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))

            weight, index = heapq.heappop(available)

            ans.append(index)

            heapq.heappush(
                busy,
                (current_time + task, weight, index)
            )

        return ans