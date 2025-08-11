'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Examples:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1], n = 1
Output: []

Дан указатель head на начало связного списка. Удалите n-й узел с конца списка и верните новый head.

Примеры:
Ввод: head = [1, 2, 3, 4, 5], n = 2
Вывод: [1, 2, 3, 5]

Ввод: head = [1], n = 1
Вывод: []
'''

from typing import Optional

class ListNode:
    def __init__(self, value: int = 0, next: Optional['ListNode'] = None):
        self.value = value
        self.next = next

def remove_nth_from_end(head: ListNode, n: int) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head

    slow = dummy
    fast = dummy

    for _ in range(n + 1):
        if fast:
            fast = fast.next
        else:
            return head

    while fast:
        slow = slow.next
        fast = fast.next

    if slow.next:
        slow.next = slow.next.next

    return dummy.next