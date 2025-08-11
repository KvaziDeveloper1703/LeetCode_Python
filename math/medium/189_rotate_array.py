'''
Given an integer array numbers, rotate the array to the right by k steps, where k is a non-negative integer.
The rotation should be done in-place, meaning you should modify the input array directly without using extra space for another array.

Examples:
Input: numbers = [1, 2, 3, 4, 5, 6, 7], k = 3
Output: [5, 6, 7, 1, 2, 3, 4]

Input: numbers = [-1, -100, 3, 99], k = 2
Output: [3, 99, -1, -100]

Дан массив целых чисел numbers и неотрицательное число k. Необходимо сдвинуть элементы массива вправо на k позиций.
Сдвиг должен быть выполнен на месте, то есть нельзя использовать дополнительный массив — нужно изменить исходный массив напрямую.

Примеры:
Ввод: numbers = [1, 2, 3, 4, 5, 6, 7], k = 3
Вывод: [5, 6, 7, 1, 2, 3, 4]

Ввод: numbers = [-1, -100, 3, 99], k = 2
Вывод: [3, 99, -1, -100]
'''

from typing import List

def rotate(numbers: List[int], k: int) -> None:
    n = len(numbers)
    k = k % n

    def reverse_part(start_index: int, end_index: int):
        while start_index < end_index:
            numbers[start_index], numbers[end_index] = numbers[end_index], numbers[start_index]
            start_index += 1
            end_index -= 1

    reverse_part(0, n - 1)
    reverse_part(0, k - 1)
    reverse_part(k, n - 1)

    return None