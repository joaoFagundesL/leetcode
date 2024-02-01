struct TreeNode **searchNode(struct TreeNode **root, int key) {
    struct TreeNode **parent = root;
    while(*parent != NULL) {
        if((*parent)->val == key)
            return parent;
        else if(key < (*parent)->val)
            parent = &((*parent)->left);
        else
            parent = &((*parent)->right);
    }
    return NULL;
}

struct TreeNode **minRightSubtree(struct TreeNode **root) {
    struct TreeNode **parent = root;
    while((*parent)->left != NULL)
        parent = &((*parent)->left);

    return parent;
}

void deleteNodeHelper(struct TreeNode** parent, int key){
    struct TreeNode *son = NULL;

    if((*parent)->left == NULL && (*parent)->right == NULL) {
        free(*parent);
        *parent = NULL;
        return;
    }
    if((*parent)->left == NULL || (*parent)->right == NULL) {
        son = (*parent)->right == NULL ? (*parent)->left : (*parent)->right;
        free(*parent);
        *parent = son;
        return;
    }
   
    struct TreeNode **minRight = minRightSubtree(&(*parent)->right);
    (*parent)->val = (*minRight)->val;
    deleteNodeHelper(minRight, (*minRight)->val);
}

struct TreeNode* deleteNode(struct TreeNode* root, int key){
    struct TreeNode **parent = searchNode(&root, key);

    if (parent == NULL || *parent == NULL) 
        return root;

    deleteNodeHelper(parent, key);
    return root;
}