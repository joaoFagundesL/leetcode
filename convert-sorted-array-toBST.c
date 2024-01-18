struct TreeNode *createNode(int val) {
    struct TreeNode *node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node->val = val;
    node->left = NULL;
    node->right = NULL;

    return node;
}

struct TreeNode* sortedArrayToBSTHelper(int* nums, int start, int end) {
    if (start > end)
        return NULL;

    int mid = start + (end - start) / 2 ;

    struct TreeNode *root = createNode(nums[mid]);

    root->left = sortedArrayToBSTHelper(nums, start, mid - 1);
    root->right = sortedArrayToBSTHelper(nums, mid + 1, end);

    return root;
} 

struct TreeNode* sortedArrayToBST(int* nums, int numsSize) {
    return sortedArrayToBSTHelper(nums, 0, numsSize - 1);
}
