# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # example [1,2,3,4,5,6]
        #
        # CALL STACK
        #  x  y      
        #  NULL => return NULL x
        # [5->6] => invert [6->5] then return x
        # [3->4] => invert [4->3] then get the return of the above call [4->3->6->5] 
        # [1->2->3->4->5->6] invert [2->1] then get the return above [2->1->4->3->6->5]
        
        if head is None or head.next is None:
            return head
        x = head
        y = x.next
        x.next = self.swapPairs(y.next)
        y.next = x
        return y
        
        
        