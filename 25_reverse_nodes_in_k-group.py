'''
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k, then the left-out nodes at the end should remain as they are.
You may not alter the values in the list's nodes, only the nodes themselves may be changed.

Examples:
Input:
head = [1,2,3,4,5], k = 2
Output:
[2,1,4,3,5]

Input:
head = [1,2,3,4,5], k = 3
Output:
[3,2,1,4,5]
'''

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverseLinkedList(start, k):
            prev, curr = None, start
            while k > 0:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                k -= 1
            return prev

        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        while length >= k:
            group_start = group_prev.next
            group_end = group_start
            for _ in range(k - 1):
                group_end = group_end.next
            
            next_group = group_end.next

            group_end.next = None
            reversed_group_head = reverseLinkedList(group_start, k)
            
            group_prev.next = reversed_group_head
            group_start.next = next_group

            group_prev = group_start

            length -= k
        
        return dummy.next