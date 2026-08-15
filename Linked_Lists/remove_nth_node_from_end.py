# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_len = 0
        original_head = head

        if head.next == None:
            return None

        while head is not None:
            list_len += 1
            head = head.next

        head = original_head

        node_id_to_remove = list_len - n - 1

        if node_id_to_remove == -1:
            original_head = head.next

        for i in range(node_id_to_remove):
            head = head.next

        head.next = None if head.next == None else head.next.next

        return original_head