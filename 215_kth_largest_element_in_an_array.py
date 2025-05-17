'''
Given an integer array numbers and an integer k, return the kth largest element in the array.
Note that the kth largest means the element that would be in the k-th position from the end if the array were sorted in ascending order. 
It does not have to be a distinct element.
Can you solve this without fully sorting the array?

Examples:
Input: numbers = [3, 2, 1, 5, 6, 4], k = 2
Output: 5

Input: numbers = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
Output: 4

Дан массив целых чисел numbers и целое число k. Требуется вернуть k-й по величине элемент в массиве.
Обратите внимание: k-й по величине означает элемент, который будет на k-м месте с конца при сортировке массива по возрастанию. 
Элемент не обязан быть уникальным.
Можно ли решить эту задачу без полной сортировки массива?

Примеры:
Ввод: numbers = [3, 2, 1, 5, 6, 4], k = 2
Вывод: 5

Ввод: numbers = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
Вывод: 4
'''

import heapq
from typing import List

def findKthLargest(number_list: List[int], k: int) -> int:
    smallest_heap_of_k_largest = number_list[:k]
    heapq.heapify(smallest_heap_of_k_largest)

    for current_number in number_list[k:]:
        if current_number > smallest_heap_of_k_largest[0]:
            heapq.heappop(smallest_heap_of_k_largest)
            heapq.heappush(smallest_heap_of_k_largest, current_number)
    
    return smallest_heap_of_k_largest[0]