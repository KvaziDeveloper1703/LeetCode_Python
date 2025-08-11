'''
Given the head of a singly linked list.

Return the node where the cycle begins. If there is no cycle, return null.

A cycle exists if a node in the list can be reached again by continuously following the next pointer.
Internally, position is used to denote the index where the tail connects to form a cycle. 
It is not passed as an argument, and you should not modify the linked list.

Examples:
Input: head = [3,2,0,-4], position = 1
Output: Node at index 1

Input: head = [1,2], position = 0
Output: Node at index 0

Дан указатель head на начало односвязного списка. 

Верните узел, в котором начинается цикл. Если цикла нет, верните null.

Цикл существует, если, следуя по next, можно попасть на уже посещённый узел.
Параметр position обозначает индекс узла, к которому соединяется хвост. 
Он не передаётся в функцию. Список нельзя модифицировать.

Примеры:
Ввод: head = [3,2,0,-4], position = 1
Вывод: Узел с индексом 1

Ввод: head = [1,2], position = 0
Вывод: Узел с индексом 0
'''

from typing import Optional

class ListNode:
    def __init__(self, value: int = 0, next: Optional['ListNode'] = None):
        self.value = value
        self.next = next

def detect_cycle(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow