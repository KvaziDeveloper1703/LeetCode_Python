'''
Given head, the head of a linked list, determine if the linked list has a cycle.
A cycle exists in the linked list if there is a node that can be revisited by continuously following the next pointer. The variable pos denotes the index of the node that the tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list, otherwise return false.

Examples:
Input:
head = [3,2,0,-4], pos = 1
Output:
true

Input:
head = [1,2], pos = 0
Output:
true
'''

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False