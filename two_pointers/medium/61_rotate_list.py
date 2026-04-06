'''
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Дан указатель head на начало отсортированного связного списка. Удалите все узлы, содержащие дубликаты — то есть оставьте только те элементы, которые встречаются один раз в исходном списке.

Верните результат в виде отсортированного связного списка.

Пример:
Ввод: head = [1, 2, 3, 3, 4, 4, 5]
Вывод: [1, 2, 5]
'''

from typing import Optional

class ListNode:
    def __init__(self, value: int = 0, next: Optional['ListNode'] = None):
        self.value = value
        self.next = next

def rotate_right(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or not head.next or k == 0:
        return head

    length = 1
    current = head

    while current.next:
        current = current.next
        length += 1

    k %= length

    if k == 0:
        return head

    current.next = head

    steps = length - k
    new_tail = head

    for _ in range(steps - 1):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None

    return new_head