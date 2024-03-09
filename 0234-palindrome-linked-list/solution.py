# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        second = self.getMiddle(head)
        second = self.reverseList(second)
        
        x1, x2 = head, second
        while x1 and x2:
            if x1.val != x2.val:
                return False
            x1, x2 = x1.next, x2.next
        return True
    
    def getMiddle(self, head):
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverseList(self, head: Optional[ListNode]):
        x = y = head.next
        head.next = None
        while x and y:
            y = x.next
            x.next = head
            head = x
            x = y
        return head
    
