# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_dum = ListNode(0)
        after_dum = ListNode(0)
        current = head
        after = after_dum
        before = before_dum
        while current:
            if current.val < x:
                before.next = current
                before = before.next
            elif current.val >= x:
                after.next = current
                after = after.next
            current = current.next
        after.next = None
        before.next = after_dum.next

        return before_dum.next

            
        