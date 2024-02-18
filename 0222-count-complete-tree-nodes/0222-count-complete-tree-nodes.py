# USING BFS
# class Solution:
#     def countNodes(self, root: Optional[TreeNode]) -> int:
#       if root is None: return 0
#       deq = collections.deque([root])
#       count = 0
#       while deq:
#         len_deq = len(deq)
#         for _ in range(len_deq):
#           n = deq.popleft()
#           count += 1
#           if n.left:
#             deq.append(n.left)
#           if n.right:
#             deq.append(n.right)
#       return count
        
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
      if root is None: return 0
      l = self.countNodes(root.left)
      r = self.countNodes(root.right)
      return l + r + 1

        