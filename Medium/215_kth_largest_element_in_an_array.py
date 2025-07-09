'''
Given an integer array numbers and an integer k.

Return the kth largest element in the array.

Note that the kth largest means the element that would be in the k-th position from the end if the array were sorted in ascending order.

Examples:
Input: numbers = [3, 2, 1, 5, 6, 4], k = 2
Output: 5

Input: numbers = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
Output: 4

Дан массив целых чисел numbers и целое число k. 

Требуется вернуть k-й по величине элемент в массиве.

Обратите внимание: k-й по величине означает элемент, который будет на k-м месте с конца при сортировке массива по возрастанию. 

Примеры:
Ввод: numbers = [3, 2, 1, 5, 6, 4], k = 2
Вывод: 5

Ввод: numbers = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
Вывод: 4
'''

import heapq
from typing import List

def find_kth_largest(numbers: List[int], k: int) -> int:
    smallest_heap_of_k_largest = numbers[:k]
    heapq.heapify(smallest_heap_of_k_largest)

    for current_number in numbers[k:]:
        if current_number > smallest_heap_of_k_largest[0]:
            heapq.heappop(smallest_heap_of_k_largest)
            heapq.heappush(smallest_heap_of_k_largest, current_number)

    return smallest_heap_of_k_largest[0]