from typing import Optional

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        list_len = 0
        curr = head
        while curr:
            list_len += 1
            curr = curr.next

        second_part = list_len // 2 + list_len % 2

        curr = head
        for _ in range(second_part - 1):
            curr = curr.next

        second_head = curr.next
        curr.next = None  

        previous = None
        curr = second_head
        while curr:
            next_node = curr.next
            curr.next = previous
            previous = curr
            curr = next_node

        first = head
        second = previous  
        while second:
            next_first = first.next
            next_second = second.next

            first.next = second
            second.next = next_first

            first = next_first
            second = next_second