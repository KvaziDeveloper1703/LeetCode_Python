'''
A linked list of length N is given, where each node contains an additional random pointer that could point to any node in the list or be null.
Construct a deep copy of the list. The deep copy should consist of exactly N brand new nodes, where each new node has its value set to the value of its corresponding original node. 
Both the next and random pointers of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. 
None of the pointers in the new list should point to nodes in the original list.
For example, if two nodes X and Y in the original list are such that X.random --> Y, then in the copied list, x.random --> y.

Return the head of the copied linked list.

Example:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
'''

from typing import Optional

class Node:
    def __init__(self, value: int, next: Optional['Node'] = None, random: Optional['Node'] = None):
        self.value = value
        self.next = next
        self.random = random

def copy_random_list(head: Optional[Node]) -> Optional[Node]:
    if not head:
        return None

    current_node = head
    while current_node:
        new_node = Node(current_node.value)
        new_node.next = current_node.next
        current_node.next = new_node
        current_node = new_node.next

    current_node = head
    while current_node:
        if current_node.random:
            current_node.next.random = current_node.random.next
        current_node = current_node.next.next

    original_node = head
    copied_node = head.next
    copied_head = head.next

    while original_node:
        original_node.next = original_node.next.next
        if copied_node.next:
            copied_node.next = copied_node.next.next
        original_node = original_node.next
        copied_node = copied_node.next

    return copied_head