'''
Given an array of integers numbers and an integer k representing the size of a sliding window.
The sliding window of size k moves from the very left of the array to the very right.
At each step, you can only see the k numbers in the window.
Each time the sliding window moves right by one position, you need to determine the maximum element in that window.

Return an array of these maximum values for all window positions.

Examples:
Input: numbers = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

Input: numbers = [1], k = 1
Output: [1]

Дан массив целых чисел numbers и размер скользящего окна k.
Скользящее окно размером k перемещается слева направо по массиву.
На каждом шаге вы видите только k элементов, находящихся в этом окне.
Каждый раз, когда окно сдвигается на одну позицию вправо, необходимо определить максимальный элемент в этом окне.

Верните массив, содержащий эти максимальные значения для всех позиций окна.

Примеры:
Ввод: numbers = [1,3,-1,-3,5,3,6,7], k = 3
Вывод: [3,3,5,5,6,7]

Ввод: numbers = [1], k = 1
Вывод: [1]
'''

from collections import deque
from typing import List

def max_sliding_window(numbers: List[int], window_size: int) -> List[int]:
    max_values = []
    index_deque = deque()

    for current_index in range(len(numbers)):
        if index_deque and index_deque[0] < current_index - window_size + 1:
            index_deque.popleft()

        while index_deque and numbers[index_deque[-1]] < numbers[current_index]:
            index_deque.pop()

        index_deque.append(current_index)

        if current_index >= window_size - 1:
            max_values.append(numbers[index_deque[0]])

    return max_values