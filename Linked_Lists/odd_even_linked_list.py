# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        odd_head = head
        even_head = head.next

        start = even_head

        turn = True
        curr = even_head.next
        while curr:
            if turn:
                odd_head.next = curr
                odd_head = curr
            else:
                even_head.next = curr
                even_head = curr
            curr = curr.next
            turn = not turn
        
        even_head.next = None
        odd_head.next = start

        return head