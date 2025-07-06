'''
Given an unsorted integer array numbers, return the smallest positive integer that is not present in numbers.
You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Examples:
Input: numbers = [1,2,0]
Output: 3

Input: numbers = [3,4,-1,1]
Output: 2

Дан неотсортированный массив целых чисел numbers. Нужно вернуть наименьшее положительное целое число, которого нет в массиве.
Вы должны реализовать алгоритм с временем выполнения O(n) и дополнительной памятью O(1).

Примеры:
Ввод: numbers = [1,2,0]
Вывод: 3

Ввод: numbers = [3,4,-1,1]
Вывод: 2
'''

from typing import List

def first_missing_positive(numbers: List[int]) -> int:
    n = len(numbers)
    
    for i in range(n):
        while 1 <= numbers[i] <= n and numbers[numbers[i] - 1] != numbers[i]:
            correct_idx = numbers[i] - 1
            numbers[i], numbers[correct_idx] = numbers[correct_idx], numbers[i]
    
    for i in range(n):
        if numbers[i] != i + 1:
            return i + 1
    return n + 1