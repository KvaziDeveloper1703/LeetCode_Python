'''
You are given head, a reference to the first node of a singly linked list.
Each node in the list contains a value of either 0 or 1. The linked list represents a binary number.
The most significant bit is stored at the head of the list.
Your task is to return the decimal value of this binary number.

Дан указатель head на первый элемент односвязного списка.
Каждый узел списка содержит значение 0 или 1. Весь список представляет двоичное число.
Старший разряд находится в начале списка.
Необходимо вернуть десятичное значение этого числа.
'''

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        result = 0
        current = head

        while current:
            result = (result << 1) | current.val
            current = current.next

        return result