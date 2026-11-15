# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        # find the middle of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow
        # # build list 1
        # r = head
        # while r.next != middle:
        #     r = r.next
        # r.next = None
        # l1 = head

        # reverse the second list to build list 2
        i, j = None, middle
        while j:
            t = j.next
            j.next = i
            i = j
            j = t
        l2 = i

        # Create new list
        while l2:
            t1, t2 = head.next, l2.next
            head.next = l2
            l2.next = t1
            head, l2 = t1, t2

        if head:
            head.next = None

