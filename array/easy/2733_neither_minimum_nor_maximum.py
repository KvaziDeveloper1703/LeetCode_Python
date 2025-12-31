'''
You are given an integer array numbers containing distinct positive integers.

Your task is to find and return any element from the array that is neither the minimum nor the maximum value in the array.

If no such element exists, return -1.

Return the selected integer.

Examples:
Input: numbers = [3,2,1,4]
Output: 2

Input: numbers = [1,2]
Output: -1

Дан массив целых чисел numbers, содержащий различные положительные числа.

Необходимо найти и вернуть любой элемент массива, который не является ни минимальным, ни максимальным значением в массиве.

Если такого элемента не существует, верните -1.

Верните выбранное число.

Примеры:
Ввод: numbers = [3,2,1,4]
Вывод: 2

Ввод: numbers = [1,2]
Вывод: -1
'''

from typing import List

def find_non_min_or_max(numbers: List[int]) -> int:
    if len(numbers) < 3:
        return -1

    minimum_value = min(numbers)
    maximum_value = max(numbers)

    for current_number in numbers:
        if current_number != minimum_value and current_number != maximum_value:
            return current_number