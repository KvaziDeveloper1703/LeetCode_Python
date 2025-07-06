'''
Given the head of a singly linked list, sort the list using insertion sort and return the head of the sorted list.

Steps of the insertion sort algorithm:
    + Insertion sort iterates through the input, consuming one element at a time and growing a sorted output list.
    + At each iteration, it removes one element from the input, finds the correct location in the sorted list, and inserts it there.
    + This repeats until all input elements have been processed.

Imagine that the sorted portion (black) initially contains only the first element. With each iteration, a new element (red) is removed from the input and inserted into the correct place in the sorted list.

Дан головной узел (head) односвязного списка. Отсортируйте этот список с помощью сортировки вставками и верните голову отсортированного списка.

Алгоритм сортировки вставками:
    + Сортировка вставками проходит по элементам списка, по одному за итерацию, и постепенно формирует отсортированный список.
    + На каждой итерации один элемент извлекается из исходного списка, находится его правильная позиция в уже отсортированной части, и элемент вставляется туда.
    + Процесс повторяется, пока не будут обработаны все элементы.

Представьте, что изначально в отсортированной части находится только первый элемент. С каждой итерацией мы берём следующий элемент из неотсортированной части и вставляем его в нужное место в уже отсортированном списке.
'''

from typing import Optional

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = head

        while current:
            previous = dummy
            while previous.next and previous.next.value < current.value:
                previous = previous.next

            next_temporary = current.next
            current.next = previous.next
            previous.next = current
            current = next_temporary

        return dummy.next