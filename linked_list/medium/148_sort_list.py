'''
Given the head of a singly linked list.

Return the list after sorting it in ascending order.

Examples:
Input: head = [4, 2, 1, 3]
Output: [1, 2, 3, 4]

Input: head = [-1, 5, 3, 4, 0]
Output: [-1, 0, 3, 4, 5]

Дан головной элемент односвязного списка.

Необходимо отсортировать список по возрастанию и вернуть голову отсортированного списка.

Примеры:
Ввод: head = [4, 2, 1, 3]
Вывод: [1, 2, 3, 4]

Ввод: head = [-1, 5, 3, 4, 0]
Вывод: [-1, 0, 3, 4, 5]
'''

from typing import Optional

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge(list_node_1: ListNode, list_node_2: ListNode) -> ListNode:
    dummy = ListNode()
    tail = dummy

    while list_node_1 and list_node_2:
        if list_node_1.value < list_node_2.value:
            tail.next, list_node_1 = list_node_1, list_node_1.next
        else:
            tail.next, list_node_2 = list_node_2, list_node_2.next
        tail = tail.next

    tail.next = list_node_1 or list_node_2
    return dummy.next

def sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    middle = slow.next
    slow.next = None

    left = self.sortList(head)
    right = self.sortList(middle)

    return self.merge(left, right)