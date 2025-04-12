'''
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Дан указатель head на начало односвязного списка и два целых числа left и right, где left <= right.
Необходимо развернуть часть списка — узлы с позиций от left до right включительно — и вернуть изменённый список.

Пример:
Вход: head = [1, 2, 3, 4, 5], left = 2, right = 4
Выход: [1, 4, 3, 2, 5]
'''

from typing import Optional

class ListNode:
    def __init__(self, value: int = 0, next: Optional['ListNode'] = None):
        self.value = value
        self.next = next

def reverse_between(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if not head or left == right:
        return head

    dummy_node = ListNode(0)
    dummy_node.next = head
    node_before_reversal = dummy_node

    for _ in range(left - 1):
        node_before_reversal = node_before_reversal.next

    reversal_start_node = node_before_reversal.next
    node_to_move = reversal_start_node.next

    for _ in range(right - left):
        reversal_start_node.next = node_to_move.next
        node_to_move.next = node_before_reversal.next
        node_before_reversal.next = node_to_move
        node_to_move = reversal_start_node.next

    return dummy_node.next