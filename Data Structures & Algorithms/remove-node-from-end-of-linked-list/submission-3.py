# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Dummy node handles edge cases (like deleting head)
        dummy = ListNode(0, head)
        find = dummy
        for _ in range(n + 1):  # move n+1 steps to maintain a gap of n between find and pre_find
            find = find.next
        
        pre_find = dummy
        while find:
            find = find.next
            pre_find = pre_find.next

        # Remove the nth node
        pre_find.next = pre_find.next.next

        return dummy.next