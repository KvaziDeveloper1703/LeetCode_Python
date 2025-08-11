'''
You are given an array of k linked-lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example:
Input: lists = [[1,4,5], 
                [1,3,4], 
                [2,6]]
Output: [1,1,2,3,4,4,5,6]

Дан массив из k отсортированных связанных списков.
Объедините все эти списки в один отсортированный связанный список и верните его.

Пример:
Ввод: lists = [ [1,4,5], 
                [1,3,4], 
                [2,6]]
Вывод: [1,1,2,3,4,4,5,6]
'''

import heapq

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value} -> {repr(self.next)}"

def merge_k_lists(lists: list[ListNode]) -> ListNode:
        min_heap = []

        for i, l in enumerate(lists):
            if l:
                heapq.heappush(min_heap, (l.value, i, l))

        dummy = ListNode(None)
        current = dummy

        while min_heap:
            value, i, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(min_heap, (node.next.value, i, node.next))

        return dummy.next