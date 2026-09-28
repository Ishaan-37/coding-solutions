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