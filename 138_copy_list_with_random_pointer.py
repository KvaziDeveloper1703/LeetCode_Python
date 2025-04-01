'''
A linked list of length n is given, where each node contains an additional random pointer that could point to any node in the list or be null.
Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointers of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.
For example, if two nodes X and Y in the original list are such that X.random --> Y, then in the copied list, x.random --> y.

Return the head of the copied linked list.

Examples:
Input:
head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output:
[[7,null],[13,0],[11,4],[10,2],[1,0]]

Input:
head = [[1,1],[2,1]]
Output:
[[1,1],[2,1]]
'''

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        current = head
        while current:
            new_node = Node(current.val)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next

        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        original = head
        copy = head.next
        copy_head = head.next
        
        while original:
            original.next = original.next.next
            if copy.next:
                copy.next = copy.next.next
            original = original.next
            copy = copy.next
        
        return copy_head