class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<>();
        postOrderHelper(root, list);
        return list;
    }

    public void postOrderHelper(TreeNode root, List<Integer> list) {
        if(root == null) 
            return;

        postOrderHelper(root.left, list);
        postOrderHelper(root.right, list);
        list.add(root.val);
    }
}
