# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:   
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:      
        while head and head.val == val:
            curr = head
            head = head.next
            del curr
            
        if not head:
            return head
            
        curr = head.next
        prev = head
        aux = curr
        while curr and aux:
            aux = curr.next
            if curr.val == val:
                prev.next = aux
                del curr
                curr = prev.next
            else:
                prev = curr
                curr = aux
        return head        
    
    
            
    
    
    
                