# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        left = 0
        right = len(arr) - 1

        max_sum = 0
        while left < right:
            if arr[left] + arr[right] > max_sum:
                max_sum = arr[left] + arr[right]
            left += 1
            right -= 1

        return max_sum