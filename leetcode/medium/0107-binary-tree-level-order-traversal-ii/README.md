# Binary Tree Level Order Traversal II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given the `root` of a binary tree, return  *the bottom-up level order traversal of its nodes' values*. (i.e., from left to right, level by level from leaf to root).

 

 **Example 1:** 

```
Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]

```

 **Example 2:** 

```
Input: root = [1]
Output: [[1]]

```

 **Example 3:** 

```
Input: root = []
Output: []

```

 

 **Constraints:** 

- The number of nodes in the tree is in the range [0, 2000].
- -1000 <= Node.val <= 1000

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 12.7 MB (beats 35.21%)  
**Submitted:** 2026-10-03T08:41:45.175Z  

```py
class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level)
        return ans[::-1]

```

---

[View on LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)