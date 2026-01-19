'''
Given the head of a singly linked list, reverse the linked list and return the new head of the reversed list.

Examples:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Дана голова односвязного списка. Нужно развернуть список в обратном порядке и вернуть новую голову перевёрнутого списка.

Примеры:
Ввод: head = [1,2,3,4,5]
Вывод: [5,4,3,2,1]

Ввод: head = [1,2]
Вывод: [2,1]
'''

from typing import Optional

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previousNode = None
        currentNode = head

        while currentNode is not None:
            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode

        return previousNode