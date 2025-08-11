'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list, which should remain sorted.

Examples:
Input:  head = [1,1,2]
Output: [1,2]

Input:  head = [1,1,2,3,3]
Output: [1,2,3]

Дан head — голова отсортированного связного списка.
Удалите все дубликаты так, чтобы каждый элемент встречался только один раз.
Верните связный список, который при этом должен остаться отсортированным.

Примеры:
Ввод:  head = [1,1,2]
Вывод: [1,2]

Ввод:  head = [1,1,2,3,3]
Вывод: [1,2,3]
'''

from typing import Optional

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    current = head
    while current and current.next:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next
    return head