# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        self.buildInOrder(root, arr)
        return self.constructBST(arr, 0, len(arr) - 1)
    
    def constructBST(self, arr, left, right) -> TreeNode:
        if left > right:
            return None
        mid = left + ((right - left) // 2)
        node = TreeNode(arr[mid])
        
        node.left = self.constructBST(arr, left, mid - 1)       
        node.right = self.constructBST(arr, mid + 1, right)
        
        return node
    
    def buildInOrder(self, root: TreeNode, arr):
        if not root:
            return
        self.buildInOrder(root.left, arr)
        arr.append(root.val)
        self.buildInOrder(root.right, arr)
        