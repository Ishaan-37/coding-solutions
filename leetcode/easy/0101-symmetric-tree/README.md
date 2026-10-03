# Symmetric Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given the `root` of a binary tree,  *check whether it is a mirror of itself*  (i.e., symmetric around its center).

 

 **Example 1:** 

```
Input: root = [1,2,2,3,4,4,3]
Output: true

```

 **Example 2:** 

```
Input: root = [1,2,2,null,3,null,3]
Output: false

```

 

 **Constraints:** 

- The number of nodes in the tree is in the range [1, 1000].
- -100 <= Node.val <= 100

 

 **Follow up:**  Could you solve it both recursively and iteratively?

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 12.7 MB (beats 31.92%)  
**Submitted:** 2026-10-03T17:27:16.674Z  

```py
class Solution(object):
    def isSymmetric(self, root):
        def mirror(a,b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            return mirror(a.left,b.right) and mirror(a.right,b.left)
        return mirror(root.left, root.right)
```

---

[View on LeetCode](https://leetcode.com/problems/symmetric-tree/)