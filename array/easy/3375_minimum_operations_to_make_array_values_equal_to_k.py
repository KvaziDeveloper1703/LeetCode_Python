'''
You are given an integer array numbers and an integer k.
An integer h is called valid if all elements in the array that are strictly greater than h have the same value.

You can perform the following operation on the array:
    - Choose a value h that is valid for the current array;
    - For every index i where numbers[i] > h, set numbers[i] = h.

Your task is to find the minimum number of operations needed to make all elements of the array equal to k. If it is impossible, return -1.

Examples:
Input: numbers = [5, 2, 5, 4, 5], k = 2
Output: 2

Input: numbers = [2, 1, 2], k = 2
Output: -1

Дан массив целых чисел numbers и число k.
Целое число h называется допустимым (valid), если все элементы массива, которые строго больше h, имеют одинаковое значение.

Вы можете выполнять следующую операцию:
    - Выбрать число h, которое допустимо для текущего массива;
    - Для каждого индекса i, где numbers[i] > h, заменить numbers[i] на h.

Необходимо найти минимальное количество операций, чтобы все элементы массива стали равны k. Если это невозможно, вернуть -1.

Примеры:
Ввод: numbers = [5, 2, 5, 4, 5], k = 2
Вывод: 2

Ввод: numbers = [2, 1, 2], k = 2
Вывод: -1
'''

from typing import List

def min_operations(numbers: List[int], target: int) -> int:
    if min(numbers) < target:
        return -1

    unique_greater_values = set()

    for value in numbers:
        if value > target:
            unique_greater_values.add(value)

    return len(unique_greater_values)