# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from collections import defaultdict

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = defaultdict(int)
        if head is None:
            return False
        while head.next is not None:
            if visited[head] == 1:
                return True
            visited[head] = 1
            head = head.next
        return False

        