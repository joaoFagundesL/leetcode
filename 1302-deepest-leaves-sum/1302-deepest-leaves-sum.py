# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        max_depth = self.getMaxDepth(root)
        hash_bfs = {}
        deq = collections.deque([root])
        
        level = 1
        while deq:
            deq_size = len(deq)
            for _ in range(deq_size):
                node = deq.popleft()
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
                    
                if level in hash_bfs:
                    hash_bfs[level].append(node.val)
                else:
                    hash_bfs[level] = [node.val]
               
            level += 1
           
        return sum(hash_bfs[max_depth])
        
    
    def getMaxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.getMaxDepth(root.left), self.getMaxDepth(root.right))