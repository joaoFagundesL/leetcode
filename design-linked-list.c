typedef struct node {
  int val;
  struct node * next;
}
Node;

typedef struct {
  struct node * head;
}
MyLinkedList;

MyLinkedList * myLinkedListCreate() {
  MyLinkedList * list = (MyLinkedList * ) malloc(sizeof(MyLinkedList));
  assert(list != NULL);
  list->head = NULL;
  return list;
}

int getLength(MyLinkedList * obj) {
  if(obj->head == NULL) 
    return 0;

  int len = 1;
  Node * curr = obj->head;

  while (curr->next != NULL) {
    curr = curr -> next;
    len++;
  }
  return len;
}

int myLinkedListGet(MyLinkedList * obj, int index) {
    int len = getLength(obj);
    if(index >= len || index < 0)
        return -1;
    
    Node *curr = obj->head;
    while(index != 0) {
        curr = curr->next;
        index--;
    }

    return curr->val;
}

void myLinkedListAddAtHead(MyLinkedList * obj, int val) {
  Node *node = (Node * ) malloc(sizeof(Node));
  assert(node != NULL);
  node->val = val;
  node->next = obj->head;
  obj->head = node;
}

void myLinkedListAddAtTail(MyLinkedList * obj, int val) {
  if(obj->head == NULL) {
    myLinkedListAddAtHead(obj, val);
    return;
  }

  Node * last = obj->head;

  while (last->next != NULL)
    last = last->next;

  Node * node = (Node * ) malloc(sizeof(Node));
  assert(node != NULL);
  node->val = val;
  node->next = NULL;
  last->next = node;
}

void myLinkedListInsertMiddle(MyLinkedList *obj, int index, int val) {
  Node *curr = obj->head;
  Node *prev;

  while (index != 0) {
    index--;
    prev = curr;
    curr = curr->next;
  }

  Node * node = (Node * ) malloc(sizeof(Node));
  assert(node != NULL);
  node->val = val;
  node->next = prev->next;
  prev->next = node;
}

void myLinkedListAddAtIndex(MyLinkedList * obj, int index, int val) {
  if (index == 0) {
    myLinkedListAddAtHead(obj, val);
    return;
  }

  int len = getLength(obj);
  if (index > len || index < 0)
    return;

  if (index == len) {
    myLinkedListAddAtTail(obj, val);
    return;
  }
  
  myLinkedListInsertMiddle(obj, index, val);
}

void myLinkedListDeleteAtHead(MyLinkedList *obj) {
    if(obj->head == NULL)
      return;
    
    Node *curr = obj->head;
    obj->head = obj->head->next;
    curr->next = NULL;
    free(curr);
}

void myLinkedListDeleteAtTail(MyLinkedList *obj) {
    if(obj->head == NULL)
      return;
    if(obj->head->next == NULL) {
      free(obj->head);
      obj->head = NULL;
      return;
    }
    
    Node *curr = obj->head;
    Node *prev;

    while(curr->next != NULL) {
      prev = curr;
      curr = curr->next;
    }

    prev->next = NULL;
    free(curr);
}

void myLinkedListDeleteMiddle(MyLinkedList *obj, int index) {
    if(obj->head == NULL)
      return;
    
    Node *curr = obj->head, *prev;

    while(index != 0) {
        index--;
        prev = curr;
        curr = curr->next;
    }

    prev->next = curr->next;
    curr->next = NULL;
    free(curr);
}

void myLinkedListDeleteAtIndex(MyLinkedList * obj, int index) {
    int len = getLength(obj);

    if(index >= len || index < 0) 
        return;
    
    if(index == 0) {
        myLinkedListDeleteAtHead(obj);
        return;
    }

    if(index == len - 1) {
        myLinkedListDeleteAtTail(obj);
        return;
    }

    myLinkedListDeleteMiddle(obj, index);
}

void myLinkedListFree(MyLinkedList * obj) {
    Node *curr;

    while(obj->head != NULL) {
      curr = obj->head;
      obj->head = obj->head->next;
      free(curr);
    }
}
