'''
Given the head of a singly linked list, return True if the list is a palindrome, or False otherwise.
A linked list is a palindrome if the sequence of its values reads the same forward and backward.

Examples:
Input: head = [1, 2, 2, 1]
Output: True

Input: head = [1, 2]
Output: False

Дан головной узел (head) односвязного списка. Верните True, если список является палиндромом, и False — в противном случае.
Список считается палиндромом, если значения его элементов читаются одинаково слева направо и справа налево.

Примеры:
Ввод: head = [1, 2, 2, 1]
Вывод: True

Ввод: head = [1, 2]
Вывод: False
'''

from typing import Optional

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def is_palindrome(head: Optional[ListNode]) -> bool:
    values = []
    current = head

    while current:
        values.append(current.value)
        current = current.next

    return values == values[::-1]