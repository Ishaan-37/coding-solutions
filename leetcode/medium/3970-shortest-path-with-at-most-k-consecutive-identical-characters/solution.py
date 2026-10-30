import heapq
from collections import defaultdict

class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))

        # state: (node, run) where run = consecutive identical chars ending at node
        dist = {(0, 1): 0}
        heap = [(0, 0, 1)]  # (cost, node, run)

        while heap:
            d, u, run = heapq.heappop(heap)
            if dist.get((u, run), float('inf')) < d:
                continue
            if u == n - 1:
                return d  # first pop of target is the minimum
            for v, w in graph[u]:
                if labels[v] == labels[u]:
                    nrun = run + 1
                    if nrun > k:
                        continue
                else:
                    nrun = 1
                nd = d + w
                if nd < dist.get((v, nrun), float('inf')):
                    dist[(v, nrun)] = nd
                    heapq.heappush(heap, (nd, v, nrun))

        return -1