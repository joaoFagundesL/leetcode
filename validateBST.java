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

    public void buildArray(TreeNode root, List<Integer> inOrderArray ) {
        if (root == null)
            return;
        
        buildArray(root.left, inOrderArray);
        inOrderArray.add(root.val);
        buildArray(root.right, inOrderArray);
    }

    public boolean isValidBST(TreeNode root) {
        List<Integer> inOrderArray = new ArrayList<Integer>();

        buildArray(root, inOrderArray);

        for (int i = 0; i < inOrderArray.size() - 1; i++) {
            if (inOrderArray.get(i + 1) <= inOrderArray.get(i))
                return false;
        }

        return true;
    }
}
