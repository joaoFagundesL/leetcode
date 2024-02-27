class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None

        if root1 and root2:
            root3 = TreeNode(root1.val + root2.val)
            root3.left = self.mergeTrees(root1.left, root2.left)
            root3.right = self.mergeTrees(root1.right, root2.right)
        elif root1:
            root3 = TreeNode(root1.val)
            root3.left = self.mergeTrees(root1.left, None)
            root3.right = self.mergeTrees(root1.right, None)
        elif root2:
            root3 = TreeNode(root2.val)
            root3.left = self.mergeTrees(None, root2.left)
            root3.right = self.mergeTrees(None, root2.right)
        return root3