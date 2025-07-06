'''
Given head, the head of a linked list, determine if the linked list has a cycle.
A cycle exists in the linked list if there is a node that can be revisited by continuously following the next pointer. 
The variable position denotes the index of the node that the tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list, otherwise return false.

Example:
Input: head = [3,2,0,-4], position = 1
Output: true

Дан указатель head на начало связного списка. Необходимо определить, содержит ли список цикл.
Цикл существует, если в списке есть такой узел, к которому можно вернуться, непрерывно переходя по указателю next.
Переменная position указывает индекс узла, на который ссылается next последнего элемента списка. Обратите внимание, что pos не передаётся как параметр — он используется только для пояснения примера.
Верните true, если в связном списке есть цикл, и false — если цикла нет.

Пример:
Вход: head = [3, 2, 0, -4], position = 1
Выход: true
'''

from typing import Optional

class ListNode:
    def __init__(self, value: int = 0, next: Optional['ListNode'] = None):
        self.value = value
        self.next = next

def has_cycle(head: Optional[ListNode]) -> bool:
    slow_pointer = head
    fast_pointer = head

    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

        if slow_pointer == fast_pointer:
            return True

    return False