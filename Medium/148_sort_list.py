'''
Given the head of a singly linked list, return the list after sorting it in ascending order.

Examples:
Input: head = [4, 2, 1, 3]
Output: [1, 2, 3, 4]

Input: head = [-1, 5, 3, 4, 0]
Output: [-1, 0, 3, 4, 5]

Дан головной элемент односвязного списка (head). Необходимо отсортировать список по возрастанию и вернуть голову отсортированного списка.

Примеры:
Ввод: head = [4, 2, 1, 3]
Вывод: [1, 2, 3, 4]

Ввод: head = [-1, 5, 3, 4, 0]
Вывод: [-1, 0, 3, 4, 5]
'''

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None
        
        left = self.sortList(head)
        right = self.sortList(mid)
        
        return self.merge(left, right)

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next
        
        tail.next = l1 or l2
        return dummy.next