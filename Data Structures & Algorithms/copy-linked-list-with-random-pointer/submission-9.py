"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        i = j = head
        dummy = Node(0, None, None)
        dummy.next = Node(0, None, None)
        node_p = random_p = dummy.next
        hash_map = defaultdict(Node)
        while i:
            node_p.val = i.val
            hash_map[i] = node_p # original_node -> copy_node
            if i.next:
                i = i.next
                node_p.next = Node(0, None, None)
                node_p = node_p.next
            else:
                break
        
        while j:
            copy_node = hash_map[j]   
            copy_node_s_random = hash_map.get(j.random)
            copy_node.random = copy_node_s_random
            j = j.next

        return dummy.next
        



        