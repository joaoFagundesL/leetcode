struct TreeNode **search(struct TreeNode **root, int val) {
    struct TreeNode **parent = root;

    while(*parent != NULL) {
        if(val < (*parent)->val) 
            parent = &((*parent)->left);
        else if(val > (*parent)->val)
            parent = &((*parent)->right);
    }
    
    return parent;
}

struct TreeNode* insertIntoBST(struct TreeNode* root, int val){
    
    struct TreeNode **parent = search(&root, val);
    
    struct TreeNode *node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node->val = val;
    node->left = NULL;
    node->right = NULL;
    *parent = node;

    return root;
}
