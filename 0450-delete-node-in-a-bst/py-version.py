class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            right_subtree = root.right
            while right_subtree.left:
                right_subtree = right_subtree.left
            
            root.val = right_subtree.val
            root.right = self.deleteNode(root.right, right_subtree.val)
        return root
