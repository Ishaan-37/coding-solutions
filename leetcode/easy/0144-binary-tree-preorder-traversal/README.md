# Binary Tree Preorder Traversal

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given the `root` of a binary tree, return  *the preorder traversal of its nodes' values*.

 

 **Example 1:** 

 **Input:**  root = [1,null,2,3]

 **Output:**  [1,2,3]

 **Explanation:** 

 **Example 2:** 

 **Input:**  root = [1,2,3,4,5,null,8,null,null,6,7,9]

 **Output:**  [1,2,4,5,6,7,3,8,9]

 **Explanation:** 

 **Example 3:** 

 **Input:**  root = []

 **Output:**  []

 **Example 4:** 

 **Input:**  root = [1]

 **Output:**  [1]

 

 **Constraints:** 

- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

 

 **Follow up:**  Recursive solution is trivial, could you do it iteratively?

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 12.5 MB (beats 39.95%)  
**Submitted:** 2026-09-28T16:02:41.123Z  

```py

class Solution(object):
    def preorderTraversal(self, root):
        ans = []
        def dfs(root):
            if not root:
                return
            ans.append(root.val)    # ROOT
            dfs(root.left)          # LEFT
            dfs(root.right)         # RIGHT
        dfs(root)
        return ans
```

---

[View on LeetCode](https://leetcode.com/problems/binary-tree-preorder-traversal/)