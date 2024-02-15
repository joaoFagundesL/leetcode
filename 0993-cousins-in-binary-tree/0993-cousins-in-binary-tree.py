class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False
        
        my_hash, deq = {}, collections.deque()
        deq.append((root, None))
        
        level = 0
        while deq:
            deq_len = len(deq)            
            # check all neighbors from the elements in the queue 
            # tree does not have cycle, hence don't need to keep track of visited nodes
            for _ in range(deq_len):
                node, node_parent = deq.popleft()
                if node.left:
                    deq.append((node.left, node.val))
                if node.right:
                    deq.append((node.right, node.val))
                my_hash[node.val] = (level, node_parent)
            level += 1
        if (my_hash[x][0] == my_hash[y][0]) and (my_hash[x][1] != my_hash[y][1]): 
            return True
        return False
                                                                 
                    