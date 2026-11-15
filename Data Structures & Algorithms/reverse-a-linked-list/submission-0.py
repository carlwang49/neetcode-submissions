# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # None
        if head == None or head.next == None:
            return head
        i = None
        j = head
        k = head.next
        while k != None:
            j.next = i
            i = j
            j = k
            k = k.next
        j.next = i
        return j
            