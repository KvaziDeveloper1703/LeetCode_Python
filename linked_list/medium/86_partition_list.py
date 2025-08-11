'''
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Examples:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Дан указатель head на начало связного списка и значение x. Необходимо перестроить список так, чтобы все узлы с значениями меньше x шли перед узлами с значениями, большими или равными x.
При этом нужно сохранить исходный относительный порядок узлов в каждой из двух частей.

Пример:
Ввод: head = [1, 4, 3, 2, 5, 2], x = 3
Вывод: [1, 2, 2, 4, 3, 5]
'''

from typing import Optional

class ListNode:
    def __init__(self, value: int = 0, next: Optional['ListNode'] = None):
        self.value = value
        self.next = next

def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    less_head = ListNode(0)
    greater_head = ListNode(0)

    less = less_head
    greater = greater_head
    current = head

    while current:
        if current.value < x:
            less.next = current
            less = less.next
        else:
            greater.next = current
            greater = greater.next
        current = current.next

    greater.next = None
    less.next = greater_head.next

    return less_head.next