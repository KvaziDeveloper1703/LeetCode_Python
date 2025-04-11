'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each node contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zeros, except the number 0 itself.

Examples:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]

Input: l1 = [0], l2 = [0]
Output: [0]

Даны два непустых связных списка, представляющих два неотрицательных числа. Цифры хранятся в обратном порядке, и каждый узел содержит одну цифру. Необходимо сложить эти два числа и вернуть результат в виде связного списка.
Можно предположить, что оба числа не содержат ведущих нулей, за исключением самого числа 0.

Примеры:
Вход: list_1 = [2, 4, 3], list_2 = [5, 6, 4]
Выход: [7, 0, 8]

Вход: list_1 = [0], list_2 = [0]
Выход: [0]
'''

from typing import Optional

class ListNode:
    def __init__(self, value: int = 0, next: Optional['ListNode'] = None):
        self.value = value
        self.next = next

def add_two_numbers(list_1: ListNode, list_2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        carry = 0

        while list_1 or list_2 or carry:
            value_1 = list_1.value if list_1 else 0
            value_2 = list_2.value if list_2 else 0
            
            total = value_1 + value_2 + carry
            
            carry = total // 10
            
            current.next = ListNode(total % 10)
            current = current.next
            
            if list_1:
                list_1 = list_1.next
            if list_2:
                list_2 = list_2.next
        
        return dummy.next