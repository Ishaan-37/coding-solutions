# Binary Tree Postorder Traversal

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given the `root` of a binary tree, return  *the postorder traversal of its nodes' values*.

 

 **Example 1:** 

 **Input:**  root = [1,null,2,3]

 **Output:**  [3,2,1]

 **Explanation:** 

 **Example 2:** 

 **Input:**  root = [1,2,3,4,5,null,8,null,null,6,7,9]

 **Output:**  [4,6,7,5,2,9,8,3,1]

 **Explanation:** 

 **Example 3:** 

 **Input:**  root = []

 **Output:**  []

 **Example 4:** 

 **Input:**  root = [1]

 **Output:**  [1]

 

 **Constraints:** 

- The number of the nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

 

 **Follow up:**  Recursive solution is trivial, could you do it iteratively?

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 12.4 MB (beats 23.05%)  
**Submitted:** 2026-09-28T16:04:49.199Z  

```py
class Solution(object):
    def postorderTraversal(self, root):
        ans = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)          # LEFT
            dfs(root.right)         # RIGHT
            ans.append(root.val)    # ROOT
        dfs(root)
        return ans
```

---

[View on LeetCode](https://leetcode.com/problems/binary-tree-postorder-traversal/)