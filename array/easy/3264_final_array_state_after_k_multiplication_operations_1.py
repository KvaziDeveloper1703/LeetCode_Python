'''
You are given an integer array numbers, an integer k, and an integer multiplier.

You must perform exactly k operations on the array. In each operation:
    - Find the minimum value x in numbers;
    - If the minimum value occurs multiple times, choose the one with the smallest index;
    - Replace that element x with x × multiplier.

Return the final array after performing all k operations.

Examples:
Input: numbers = [2,1,3,5,6], k = 5, multiplier = 2
Output: [8,4,6,5,6]

Input: numbers = [1,2], k = 3, multiplier = 4
Output: [16,8]

Дан целочисленный массив numbers, целое число k и целое число multiplier.

Нужно выполнить ровно k операций над массивом. В каждой операции:
    - Найти минимальный элемент x в массиве numbers;
    - Если минимальный элемент встречается несколько раз, выбрать тот, который стоит раньше всех;
    - Заменить выбранный элемент x на x × multiplier.

Верните массив numbers после выполнения всех k операций.

Примеры:
Ввод: numbers = [2,1,3,5,6], k = 5, multiplier = 2
Вывод: [8,4,6,5,6]

Ввод: numbers = [1,2], k = 3, multiplier = 4
Вывод: [16,8]
'''

from typing import List
import heapq

def get_final_state(numbers: List[int], k: int, multiplier: int) -> List[int]:
    minimum_heap = []

    for index in range(len(numbers)):
        heapq.heappush(minimum_heap, (numbers[index], index))

    for _ in range(k):
        minimum_value, minimum_index = heapq.heappop(minimum_heap)
        new_value = minimum_value * multiplier
        numbers[minimum_index] = new_value
        heapq.heappush(minimum_heap, (new_value, minimum_index))

    return numbers