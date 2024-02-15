# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        deq, ans = collections.deque([root]), []
        total, count = 0, 0
        while deq:
            deq_len = len(deq)
            for _ in range(deq_len):
                node = deq.popleft()
                total += node.val
                count += 1
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
                    
            ans.append(total / count)
            count = 0
            total = 0
        
        return ans
                    