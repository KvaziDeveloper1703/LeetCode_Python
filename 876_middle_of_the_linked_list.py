"""
You are given the head of a singly linked list. Return the middle node of the linked list.
If the list has an even number of nodes, return the second of the two middle nodes.
Return the middle node along with all the nodes that follow it.

Examples:

Input: head = [1, 2, 3, 4, 5]
Output: [3, 4, 5]

Input: head = [1, 2, 3, 4, 5, 6]
Output: [4, 5, 6]
"""

class ListNode(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution(object):
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow