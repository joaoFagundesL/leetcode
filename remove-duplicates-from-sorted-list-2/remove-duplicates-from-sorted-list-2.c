/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head){
   if(head == NULL) { return NULL; }

   struct ListNode* curr = head;

   struct ListNode* prev = (struct ListNode*)malloc(sizeof(struct ListNode));
   prev->next = head;
   prev->val = 0;

   struct ListNode *dummy = prev;

   while(curr != NULL && curr->next != NULL) {
       if(curr->val != curr->next->val) {
           curr = curr->next;
           dummy = dummy->next;
        } else if(curr->val == curr->next->val) {

            while(curr->next != NULL && curr->val == curr->next->val) 
                curr = curr->next;
            
            dummy->next = curr->next;
            curr = curr->next;
        }
   }

   return prev->next;
} 
