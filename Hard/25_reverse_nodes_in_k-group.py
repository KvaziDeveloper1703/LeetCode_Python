'''
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
K is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k, then the left-out nodes at the end should remain as they are.
You may not alter the values in the list's nodes, only the nodes themselves may be changed.

Examples:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Дан указатель head на начало связного списка. Необходимо разворачивать узлы списка по k штук, и вернуть изменённый список.
K — положительное целое число, не превышающее длину списка.
Если количество узлов в списке не делится на k, то оставшиеся узлы в конце остаются без изменений.
Нельзя изменять значения в узлах — можно менять только сами узлы.

Примеры:
Ввод: head = [1, 2, 3, 4, 5], k = 2
Вывод: [2, 1, 4, 3, 5]

Ввод: head = [1, 2, 3, 4, 5], k = 3
Вывод: [3, 2, 1, 4, 5]
'''

from typing import Optional

class ListNode:
    def __init__(self, value: int = 0, next: Optional['ListNode'] = None):
        self.value = value
        self.next = next

def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    def reverse_linked_list(start: ListNode, k: int) -> ListNode:
        previous, current = None, start
        while k > 0:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
            k -= 1
        return previous

    dummy = ListNode(0)
    dummy.next = head
    group_previous = dummy

    while True:
        kth = group_previous
        count = 0
        while count < k and kth:
            kth = kth.next
            count += 1
        if not kth:
            break

        group_start = group_previous.next
        group_end = kth.next
        kth.next = None

        new_group_head = reverse_linked_list(group_start, k)
        group_previous.next = new_group_head
        group_start.next = group_end
        group_previous = group_start

    return dummy.next