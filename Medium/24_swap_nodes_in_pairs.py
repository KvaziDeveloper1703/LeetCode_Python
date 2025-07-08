'''
Given a singly linked list, swap every two adjacent nodes and return its head.
You must not modify the values in the nodes—only the nodes themselves can be changed.

Examples:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Input: head = []
Output: []

Дан односвязный список. Поменяйте местами каждые две соседние вершины и верните новый head списка.
Нельзя изменять значения в самих узлах — разрешено только переставлять узлы.

Примеры:
Ввод: head = [1,2,3,4]
Вывод: [2,1,4,3]

Ввод: head = []
Вывод: []
'''

from typing import Optional

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)  
    dummy.next = head
    previous = dummy

    while head and head.next:
        first = head
        second = head.next

        previous.next = second
        first.next = second.next
        second.next = first

        previous = first
        head = first.next

    return dummy.next