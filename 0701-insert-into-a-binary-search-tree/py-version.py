class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        parent = self.search(root, val)
        node = TreeNode(val)
        if not parent:
            return node
        if node.val < parent.val:
            parent.left = node
        else:
            parent.right = node
        return root

    def search(self, root: Optional[TreeNode], val: int):
        parent = root
        aux = None
        while parent:
            aux = parent
            if val < parent.val:
                parent = parent.left
            elif val > parent.val:
                parent = parent.right
        return aux
