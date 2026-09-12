# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None

        size = 0
        copy = head
        while copy:
            size += 1
            copy = copy.next
        print(size)

        to_delete = (size // 2)

        copy = head
        for _ in range(to_delete - 1):
            copy = copy.next
        
        copy.next = copy.next.next

        return head