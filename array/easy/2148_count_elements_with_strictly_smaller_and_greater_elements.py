'''
Given an integer array numbers, return the number of elements that have both a strictly smaller element and a strictly greater element somewhere in the array.

In other words, count how many elements x satisfy:
    - there exists some element < x in numbers;
    - there exists some element > x in numbers.

Examples:
Input: numbers = [11, 7, 2, 15]
Output: 2

Input: numbers = [-3, 3, 3, 90]
Output: 2

Дан массив целых чисел numbers. Нужно вернуть количество элементов, для которых есть хотя бы один элемент строго меньше и хотя бы один элемент строго больше в этом массиве.

То есть нужно посчитать, сколько элементов x удовлетворяют условиям:
    - в массиве есть элемент < x;
    - в массиве есть элемент > x.

Примеры:
Ввод: numbers = [11, 7, 2, 15]
Вывод: 2

Ввод: numbers = [-3, 3, 3, 90]
Вывод: 2
'''

from typing import List

def count_elements(numbers: List[int]) -> int:
    min_value = min(numbers)
    max_value = max(numbers)
    count_elements_between_min_and_max = 0

    for current_number in numbers:
        if min_value < current_number < max_value:
            count_elements_between_min_and_max += 1

    return count_elements_between_min_and_max