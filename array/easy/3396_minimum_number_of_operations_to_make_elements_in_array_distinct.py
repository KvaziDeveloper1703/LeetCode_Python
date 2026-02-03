'''
You are given an integer array numbers. Your goal is to make all elements in the array distinct.

You are allowed to perform the following operation any number of times:
    - Remove the first 3 elements from the array;
    - If fewer than 3 elements remain, remove all remaining elements.

An empty array is considered to have distinct elements.
Return the minimum number of operations required to make all elements in the array distinct.

Examples:
Input: numbers = [1, 2, 3, 4, 2, 3, 3, 5, 7]
Output: 2

Input: numbers = [4, 5, 6, 4, 4]
Output: 2

Дан массив целых чисел numbers. Нужно сделать так, чтобы все элементы массива были различными.

Разрешена следующая операция, которую можно выполнять сколько угодно раз:
    - Удалить первые 3 элемента массива;
    - Если осталось меньше 3 элементов, удалить все оставшиеся.

Пустой массив считается массивом с различными элементами.
Верните минимальное количество операций, необходимое, чтобы элементы массива стали различными.

Примеры:
Ввод: numbers = [1, 2, 3, 4, 2, 3, 3, 5, 7]
Вывод: 2

Ввод: numbers = [4, 5, 6, 4, 4]
Вывод: 2
'''

from typing import List

def minimum_operations(numbers: List[int]) -> int:
    array_length = len(numbers)

    for operations in range((array_length + 2) // 3 + 1):
        start_index = operations * 3

        if start_index >= array_length:
            return operations

        remaining_part = numbers[start_index:]

        if len(remaining_part) == len(set(remaining_part)):
            return operations

    return 0