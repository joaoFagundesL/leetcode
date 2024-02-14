class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:  
        l = []
        self.helper(root, l)
        return l[k-1]
    
    def helper(self, root: Optional[TreeNode], l: List) -> Optional[int]:  
        if not root:
            return
        self.helper(root.left, l)
        l.append(root.val)
        self.helper(root.right, l)
        
        # follow up: keep a list from inorder and store the node and the information
        # of what kth is that element. Every time I remove an element i get the the information
        # of the node and update. Eg: 10-1 20-2 30-3 40-4 50-5 if i want to remove 40, i know
        # it's the 4 kth element so i just need to update from 40 until the end 10-1 20-2 40-3 50-4