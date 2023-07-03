/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head){

    if(head == NULL || head->next == NULL) { return head; }
    
    struct ListNode *unique = head->next;
    struct ListNode *x = head, *tmp = head;

    /*unique = 1; list[i] != list[i+1] if true list[unique] = list[i+1]; unique++; */
    while(x->next != NULL) {
        if(x->val != x->next->val) {
           unique->val = x->next->val;
           tmp = unique;
           unique = unique->next;
        }

        x = x->next;
    }

    /* the {k} first elements are unique, the rest is useless, so i can set the pointer as null to remove the link */
    tmp->next = NULL;
    return head;
}


