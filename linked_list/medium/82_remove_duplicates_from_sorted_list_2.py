'''
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. 

Return the linked list sorted as well.

Example:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Дан указатель head на начало отсортированного связного списка. Необходимо удалить все узлы, содержащие повторяющиеся значения, оставив в списке только уникальные числа, которые встречаются только один раз в исходном списке.

Верните отсортированный связный список после удаления дубликатов.

Пример:
Ввод: head = [1, 2, 3, 3, 4, 4, 5]
Вывод: [1, 2, 5]
'''

from typing import Optional

class ListNode:
    def __init__(self, value: int = 0, next: Optional['ListNode'] = None):
        self.value = value
        self.next = next

def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head
    previous = dummy

    while head:
        if head.next and head.value == head.next.value:
            while head.next and head.value == head.next.value:
                head = head.next
            previous.next = head.next
        else:
            previous = previous.next
        head = head.next

    return dummy.next