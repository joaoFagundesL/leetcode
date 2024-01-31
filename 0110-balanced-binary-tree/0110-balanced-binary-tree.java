/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isBalanced(TreeNode root) {
      int ans = isBalancedHelper(root);
      
      if (ans == -1) return false;
      
      return true;
    }
  
    public int isBalancedHelper(TreeNode root) {
      if (root == null)
        return 0;
      
      int l = isBalancedHelper(root.left);
      int r = isBalancedHelper(root.right);
      
      int bf = Math.abs(l - r);
      
      if (bf > 1 || l == -1 || r == -1)
        return -1;
       
      return Math.max(l, r) + 1;
    }
    
}