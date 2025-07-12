'''
Given an integer array numbers, reorder it so that: numbers[0] < numbers[1] > numbers[2] < numbers[3] > ...
You may assume that the input array always has a valid answer.

Examples:
Input: numbers = [1,5,1,1,6,4]
Output: [1,6,1,5,1,4]

Input: numbers = [1,3,2,2,3,1]
Output: [2,3,1,3,1,2]

Дан массив целых чисел numbers. Необходимо переставить его элементы так, чтобы выполнялось: numbers[0] < numbers[1] > numbers[2] < numbers[3] > ...
Можно считать, что для входного массива всегда существует корректное решение.

Примеры:
Ввод: numbers = [1,5,1,1,6,4]
Вывод: [1,6,1,5,1,4]

Ввод: numbers = [1,3,2,2,3,1]
Вывод: [2,3,1,3,1,2]
'''

from typing import List

def wiggle_sort(numbers: List[int]) -> None:
    sorted_numbers = sorted(numbers)
    n = len(numbers)
    middle = (n + 1) // 2

    left = sorted_numbers[:middle][::-1]
    right = sorted_numbers[middle:][::-1]

    numbers[::2] = left
    numbers[1::2] = right