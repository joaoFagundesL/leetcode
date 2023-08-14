struct TreeNode **search(struct TreeNode **root, int val) {
  struct TreeNode **p = root;
  while(*p != NULL) {
    if(val < (*p)->val)
      p = &((*p)->left);
    else
      p = &((*p)->right);
  }

  return p;
}

void insert(struct TreeNode **root, int val) {
  struct TreeNode *node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
  assert(node != NULL);
  node->left = NULL;
  node->right = NULL;
  node->val = val;

  struct TreeNode **parent = search(root, val);
  *parent = node; 
}

struct TreeNode* bstFromPreorder(int* preorder, int preorderSize){
  struct TreeNode **root = NULL;
  for(int i = 0; i < preorderSize; i++) 
    insert(&root, preorder[i]);

  return root;
}
