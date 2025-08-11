'''
A linked list of length N is given, where each node contains an additional pointer random, which may point to any node in the list or be null.

It is required to construct a deep copy of this list. The deep copy should consist of exactly N completely new nodes, in which:
    + the value of each new node matches the value of the corresponding node in the original list,
    + the next and random pointers of the new nodes should point to new nodes in the copied list so that the structure of connections fully replicates the structure of the original list,
    + none of the pointers in the new list should point to nodes from the original list.

For example, if there are two nodes X and Y in the original list such that X.random --> Y, then in the copied list for the corresponding nodes x and y it must hold that x.random --> y.

You need to return the head of the new (copied) linked list.

Example:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Дана связанная (однонаправленная) список длины N, где каждый узел содержит дополнительный указатель random, который может указывать на любой узел в списке или быть равен null.

Необходимо построить глубокую копию этого списка. Глубокая копия должна состоять ровно из N совершенно новых узлов, в которых:
    + значение каждого нового узла совпадает со значением соответствующего узла исходного списка,
    + указатели next и random новых узлов должны указывать на новые узлы в скопированном списке так, чтобы структура связей полностью повторяла структуру исходного списка,
    + никакие указатели в новом списке не должны указывать на узлы исходного списка.

Например, если в исходном списке два узла X и Y такие, что X.random --> Y, то в скопированном списке для соответствующих узлов x и y должно выполняться x.random --> y. 

Нужно вернуть голову нового (скопированного) связанного списка.

Пример:
Ввод: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Вывод: [[7,null],[13,0],[11,4],[10,2],[1,0]]
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