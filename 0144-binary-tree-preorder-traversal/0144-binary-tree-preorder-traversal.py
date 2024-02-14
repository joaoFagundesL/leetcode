# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.preorderTransversalHelper(root, ans)
        return ans
    
    def preorderTransversalHelper(self, root: Optional[TreeNode], ans: List):
        if root is None:
            return root
        ans.append(root.val)
        self.preorderTransversalHelper(root.left, ans)
        self.preorderTransversalHelper(root.right, ans)
        