struct ListNode* middleNode(struct ListNode* head){
    if(head == NULL || head->next == NULL) 
        return head;
    
    struct ListNode *fast = head->next->next;
    struct ListNode *slow = head;

    while(fast != NULL) {
        if(fast->next == NULL) 
            return slow->next;
        if(fast->next->next == NULL)
            return slow->next->next;

        fast = fast->next->next;
        slow = slow->next;
    }

    return slow->next;
}
