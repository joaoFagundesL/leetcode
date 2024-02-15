# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        my_hash, deq = {}, collections.deque()
        level = 0
        deq.append(root)
        
        while deq:
            deq_len = len(deq)
            for _ in range(deq_len):
                node = deq.popleft()
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
                if level in my_hash:
                    my_hash[level].append(node.val)
                if level not in my_hash:
                    my_hash[level] = [node.val]
            level += 1
        
        return list(my_hash.values())