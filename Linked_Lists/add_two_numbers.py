# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nr = []
        carry = 0

        while l1 and l2:
            nr.append((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            nr.append((l1.val + carry) % 10)
            carry = (l1.val + carry) // 10
            l1 = l1.next
        while l2:
            nr.append((l2.val + carry) % 10)
            carry = (l2.val + carry) // 10
            l2 = l2.next
        
        if carry:
            nr.append(1)
        
        head = ListNode(nr[0])
        prev = head

        for i in range(1, len(nr)):
            new_node = ListNode(nr[i])
            prev.next = new_node
            prev = new_node
        
        return head