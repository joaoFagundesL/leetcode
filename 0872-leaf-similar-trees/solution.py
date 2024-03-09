# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        arr1, arr2 = [], []
        self.buildArr(root1, arr1)
        self.buildArr(root2, arr2)
        
        n1, n2 = len(arr1), len(arr2)
        if n1 != n2:
            return False
        
        for i in range(n1):
            if arr1[i] != arr2[i]:
                return False
        return True
    
    def buildArr(self, root: Optional[TreeNode], arr):
        if not root:
            return
        if not root.left and not root.right:
            arr.append(root.val)
            return
        self.buildArr(root.left, arr)
        self.buildArr(root.right, arr)
        
        
