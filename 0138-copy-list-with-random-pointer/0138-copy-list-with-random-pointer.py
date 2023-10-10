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
        
        # create a dictionary to map original nodes to new nodes
        node_dict = dict()
        node = head
        while node:
            node_dict[node] = Node(node.val)
            node = node.next
            
        # set next and random pointers for new nodes
        node = head
        while node:
            if node.next:
                node_dict[node].next = node_dict[node.next]
            if node.random:
                node_dict[node].random = node_dict[node.random]
            node = node.next
            
        return node_dict[head]