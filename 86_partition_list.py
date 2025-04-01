'''
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Examples:
Input:
head = [1,4,3,2,5,2], x = 3
Output:
[1,2,2,4,3,5]

Input:
head = [2,1], x = 2
Output:
[1,2]
'''

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_head = ListNode(0)
        greater_head = ListNode(0)
        
        less = less_head
        greater = greater_head
        
        current = head

        while current:
            if current.val < x:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next
            current = current.next

        less.next = greater_head.next

        greater.next = None

        return less_head.next