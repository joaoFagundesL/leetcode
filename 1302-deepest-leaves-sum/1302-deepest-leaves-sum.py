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
        hash_bfs = {}
        deq = collections.deque([root])
        level, max_level, total = 1, 1, 0
       
        while deq:
            deq_size = len(deq)
            for _ in range(deq_size):
                node = deq.popleft()

                if level > max_level:
                    total, max_level = 0, level
                total += node.val
                
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)          
            level += 1
        return total