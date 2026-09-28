
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