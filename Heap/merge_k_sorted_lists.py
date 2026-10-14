# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        dummy = ListNode()
        curr = dummy
        h = []

        for i, head in enumerate(lists):
            if head:
                heapq.heappush(h, (head.val, i, head))

        while h:
            val, i, node = heapq.heappop(h)

            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(h, (node.next.val, i, node.next))

        return dummy.next