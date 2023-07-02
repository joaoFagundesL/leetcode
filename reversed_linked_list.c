/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head){

    if(head == NULL) 
        return NULL;
    
    struct ListNode* y = head->next;
    struct ListNode* aux = y;

    // updating the end of the list
    head->next = NULL;

    while(y != NULL && aux != NULL) {

        // y is always one ahead of the head, and aux is one ahead of the y
        aux = y->next;        

        // pointing to the previous node
        y->next = head;

        // updating the head
        head = y;

        // aux can be null here so i update the head before this line.
        y = aux;
    }

    return head;
}
