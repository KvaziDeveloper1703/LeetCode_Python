'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Examples:
Input:
head = [1,2,3,4,5], n = 2
Output:
[1,2,3,5]

Input:
head = [1], n = 1
Output:
[]
'''

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next