'''
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Examples:
Input:
head = [1,2,3,4,5], left = 2, right = 4
Output:
[1,4,3,2,5]

Input:
head = [5], left = 1, right = 1
Output:
[5]
'''

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        start = prev.next
        then = start.next
        
        for _ in range(right - left):
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next

        return dummy.next
