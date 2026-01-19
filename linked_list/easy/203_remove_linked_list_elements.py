'''
Given the head of a singly linked list and an integer value, remove all nodes from the list where Node.value == value, and return the new head of the linked list.

Examples:
Input: head = [1,2,6,3,4,5,6], value = 6
Output: [1,2,3,4,5]

Input: head = [], value = 1
Output: []

Дана голова односвязного списка и целое число value. Удали все узлы списка, у которых Node.value == value, и верни новую голову списка.

Примеры:
Ввод: head = [1,2,6,3,4,5,6], value = 6
Вывод: [1,2,3,4,5]

Ввод: head = [], value = 1
Вывод: []
'''

from typing import Optional

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], value: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        currentNode = dummyNode

        while currentNode.next is not None:
            if currentNode.next.value == value:
                currentNode.next = currentNode.next.next
            else:
                currentNode = currentNode.next

        return dummyNode.next