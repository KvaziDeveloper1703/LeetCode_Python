"""
You are given the head of a singly linked list. Return the middle node of the linked list.
If the list has an even number of nodes, return the second of the two middle nodes.
Return the middle node along with all the nodes that follow it.

Examples:
Input: head = [1, 2, 3, 4, 5]
Output: [3, 4, 5]

Input: head = [1, 2, 3, 4, 5, 6]
Output: [4, 5, 6]

Дан указатель head на начало односвязного списка. Необходимо вернуть средний узел списка.
Если в списке нечётное количество узлов — верните средний элемент. Если количество узлов чётное — верните второй из двух средних.
Нужно вернуть средний узел вместе со всеми следующими за ним узлами.

Примеры:
Ввод: head = [1, 2, 3, 4, 5]
Вывод: [3, 4, 5]

Ввод: head = [1, 2, 3, 4, 5, 6]
Вывод: [4, 5, 6]
"""

class ListNode(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def middle_node(head):
    slow_pointer = fast_pointer = head
    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
    return slow_pointer