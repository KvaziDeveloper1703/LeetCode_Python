'''
Given the head of a singly linked list, return true if the list is a palindrome, or false otherwise.
A linked list is a palindrome if the sequence of its values reads the same forward and backward.

Examples:
Input: head = [1, 2, 2, 1]
Output: true

Input: head = [1, 2]
Output: false

Дан головной узел (head) односвязного списка. Верните true, если список является палиндромом, и false — в противном случае.
Список считается палиндромом, если значения его элементов читаются одинаково слева направо и справа налево.

Примеры:
Ввод: head = [1, 2, 2, 1]
Вывод: true

Ввод: head = [1, 2]
Вывод: false
'''

from typing import Optional

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def is_palindrome(self, head: Optional[ListNode]) -> bool:
        values = []

        current = head
        while current:
            values.append(current.value)
            current = current.next

        return values == values[::-1]