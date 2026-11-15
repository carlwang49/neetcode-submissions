# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1, h2, = list1, list2
        if h1 == None:
            return h2
        if h2 == None:
            return h1

        m = merge_list = ListNode()
        while h1 != None and h2 != None:
            if h1.val <= h2.val:
                m.val = h1.val
                h1 = h1.next
            else:
                m.val = h2.val
                h2 = h2.next
            if h1 != None and h2 != None:
                m.next = ListNode()
                m = m.next

        if h1 == None:
            m.next = h2
        if h2 == None:
            m.next = h1

        return merge_list
        
            