struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    struct ListNode *y = list1;
    struct ListNode *x = list2;
    struct ListNode *aux;
    
    if(y == NULL && x != NULL) return list2;

    while(x != NULL) {
        if(x->val <= list1->val) {
            aux = x->next;
            x->next = list1;
            list1 = x;
            y = x;
            x = aux;
        }else if(y->next != NULL && x->val <= y->next->val) {
            aux = x->next;
            x->next = y->next;
            y->next = x;
            x = aux;
        }else if(y->next == NULL && x->val >= y->val) {
            aux = x->next;
            y->next = x;
            x->next = NULL;
            x = aux;
        }else
            y = y->next;
    }
    return list1;
}
