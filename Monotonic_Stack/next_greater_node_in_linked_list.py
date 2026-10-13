# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode | None) -> list[int]:
        vals = []
        
        curr = head

        while curr:
            vals.append(curr.val)
            curr = curr.next
        
        st = []
        res = [0] * len(vals)

        for i, val in enumerate(vals):
            while st and val > st[-1][1]:
                curr_element_idx, curr_element_val = st.pop()
                res[curr_element_idx] = val
            st.append((i, val))
        
        return res
            
