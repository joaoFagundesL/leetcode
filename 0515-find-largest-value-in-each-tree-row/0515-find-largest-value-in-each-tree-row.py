# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        
        ans = []
        deq = collections.deque([root])
        
        while deq:
            n = len(deq)
            highest = float('-inf')
            for _ in range(n):
                node = deq.popleft()
                curr = node.val
                highest = max(highest, curr)   
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
            ans.append(highest)
        return ans
                