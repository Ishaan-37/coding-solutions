class Solution:
    def inorderTraversal(self, root):
        ans = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)          # LEFT
            ans.append(root.val)    # ROOT
            dfs(root.right)         # RIGHT
        dfs(root)
        return ans