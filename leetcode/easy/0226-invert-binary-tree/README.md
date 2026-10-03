# Invert Binary Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given the `root` of a binary tree, invert the tree, and return  *its root*.

 

 **Example 1:** 

```
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

```

 **Example 2:** 

```
Input: root = [2,1,3]
Output: [2,3,1]

```

 **Example 3:** 

```
Input: root = []
Output: []

```

 

 **Constraints:** 

- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 12.3 MB (beats 97.82%)  
**Submitted:** 2026-10-03T12:42:30.523Z  

```py
class Solution(object):
    def invertTree(self, root):
        if not root:
            return None
        root.left , root.right = root.right , root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
```

---

[View on LeetCode](https://leetcode.com/problems/invert-binary-tree/)