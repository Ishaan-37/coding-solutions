# Shortest Path With At Most K Consecutive Identical Characters

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an integer `n` representing the number of nodes in a  **directed weighted**  graph, numbered from 0 to `n - 1`. This is represented by a 2D integer array `edges`, where `edges[i] = [ui, vi, wi]` represents a directed edge from node `ui` to node `vi` with weight `wi`.

You are also given a string `labels` of length `n`, where `labels[i]` is the character assigned to node `i`, and an integer `k`.

Return the  **minimum**   **total**  edge weight of a path from node 0 to node `n - 1` such that the concatenation of the labels of the nodes along the path contains  **at most**  `k`  **consecutive**   **identical**  characters. If no valid path exists, return -1.

 

 **Example 1:** 

 **Input:**  n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 1

 **Output:**  3

 **Explanation:** 

The optimal valid path from node 0 to node 2 is as follows:

- Use edges[2] = [0, 2, 3] to reach node 2 with a weight wi = 3.
The corresponding concatenation of labels is `"ab"`, which satisfies at most `k = 1` consecutive identical characters. Thus, the answer is 3.

 **Example 2:** 

 **Input:**  n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 2

 **Output:**  2

 **Explanation:** 

The optimal valid path from node 0 to node 2 is as follows:

- Use edges[0] = [0, 1, 1] to reach node 1 with weight wi = 1.
- Use edges[1] = [1, 2, 1] to reach node 2 with weight wi = 1.
The corresponding concatenation of labels is `"aab"`, which satisfies at most `k = 2` consecutive identical characters. Thus, the answer is 2.

 **Example 3:** 

 **Input:**  n = 3, edges = [[0,1,1],[1,2,1]], labels = "aaa", k = 2

 **Output:**  -1

 **Explanation:** 

There is no valid path from node 0 to node 2 that satisfies at most `k = 2` consecutive identical characters. Thus, the answer is -1.

 

 **Constraints:** 

- 1 <= n == labels.length <= 5 * 104
- 0 <= edges.length <= 5 * 104
- edges[i] == [ui, vi, wi]
- 0 <= ui, vi <= n - 1
- ui != vi
- 1 <= wi <= 104
- labels consists of lowercase English letters
- 1 <= k <= 50

## Solution

**Language:** Python  
**Runtime:** 388 ms (beats 36.15%)  
**Memory:** 54.2 MB (beats 69.88%)  
**Submitted:** 2026-10-30T14:42:38.550Z  

```py
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
```

---

[View on LeetCode](https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/)