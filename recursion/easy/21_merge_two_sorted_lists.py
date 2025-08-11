'''
You are given the heads of two sorted linked lists list_1 and list_2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Examples:
Input: list_1 = [1,2,4], list_2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list_1 = [], list_2 = []
Output: []

Даны головы двух отсортированных связанных списков list_1 и list_2.
Объедините эти два списка в один отсортированный список. Новый список должен быть сформирован путём чередования узлов из первых двух списков.

Верните голову объединённого связанного списка.

Примеры:
Ввод: list_1 = [1, 2, 4], list_2 = [1, 3, 4]
Выход: [1, 1, 2, 3, 4, 4]

Ввод: list_1 = [], list_2 = []
Выход: []
'''

from typing import Optional

class ListNode:
    def __init__(self, value: int = 0, next: Optional['ListNode'] = None):
        self.value = value
        self.next = next

def merge_two_lists(list_1: Optional[ListNode], list_2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy

    while list_1 and list_2:
        if list_1.value < list_2.value:
            current.next = list_1
            list_1 = list_1.next
        else:
            current.next = list_2
            list_2 = list_2.next
        current = current.next

    current.next = list_1 if list_1 else list_2

    return dummy.next