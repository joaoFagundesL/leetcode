"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return root
        
        ans = []
        self.postorderHelper(root, ans)
        return ans

    def postorderHelper(self, root: 'Node', ans):
        if not root.children:
            ans.append(root.val)
            return
        
        n = len(root.children)
        for i in range(n):
            self.postorderHelper(root.children[i], ans)
        ans.append(root.val)
        
        