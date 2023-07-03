typedef struct node {
    int val;
    int min; 
    struct node *next;
}Node;

typedef struct {
  Node *top;
  int min; 
} MinStack;

MinStack* minStackCreate() {
  MinStack *obj = (MinStack*)malloc(sizeof(MinStack));

  if(obj == NULL) { return NULL; }

  obj->top = NULL;
  obj->min = INT_MAX;
  return obj;
}

Node *createNode(MinStack* obj, int val) {
  Node *node = (Node*)malloc(sizeof(Node));
  if(node == NULL) { return; }
  node->val = val;

  if(val <= obj->min) { 
    obj->min = val;
    node->min = val;
  } else
    node->min = obj->min;

  return node;
}

void minStackPush(MinStack* obj, int val) {
  Node* node = createNode(obj, val);

  if(obj->top == NULL) { 
    obj->top = node;
    node->next = NULL;
    return;
  }

  node->next = obj->top;
  obj->top = node;
}

void minStackPop(MinStack* obj) {
  if(obj->top == NULL) { return; }

  Node *tmp = obj->top;
  obj->top = tmp->next;
  
  if(obj->top != NULL) 
    obj->min = obj->top->min;
  else 
    obj->min = INT_MAX;

  free(tmp);
}

int minStackTop(MinStack* obj) {
  return obj->top->val;
}

int minStackGetMin(MinStack* obj) {
  return obj->min;
}

void minStackFree(MinStack* obj) {
  if(obj->top == NULL) { return; }

  while(obj->top != NULL) 
    minStackPop(obj);

  obj = NULL;
  free(obj);
}
