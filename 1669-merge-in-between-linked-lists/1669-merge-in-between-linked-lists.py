class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        idx = 0
        curr = list1
        prev = None
        while curr:
            prev = curr
            curr = curr.next
            idx += 1
            if idx == a:
                break
        prev.next = list2
        
        while curr:
            if idx == b:
                break
            curr = curr.next
            idx += 1
        
        curr2 = list2
        while curr2.next:
            curr2 = curr2.next
        curr2.next = curr.next
        return list1