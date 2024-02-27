# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        middle, prev = self.getMiddle(head)
        aux = middle.next
        prev.next = aux
        del middle
        return head
        
    def getMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s, f = head, head
        prev = s
        while f and f.next:
            prev = s
            s = s.next
            f = f.next.next
        return s, prev