# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # array to work as reference not value
        ans = [0]
        self.dfs(root, ans)
        return ans[0]
    
    def dfs(self, root: Optional[TreeNode], ans) -> int:
        if not root:
            return 0
        l = self.dfs(root.left, ans)
        r = self.dfs(root.right, ans)
        # sum both left and right to get diameter
        ans[0] = max(ans[0], l + r)
        # max depth
        return max(l, r) + 1
    
        