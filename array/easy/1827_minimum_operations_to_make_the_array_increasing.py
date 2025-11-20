'''
You are given an integer array numbers.
In one operation, you may choose any element of the array and increase its value by 1.

Your task is to return the minimum number of operations required to make the array strictly increasing.

An array numbers is strictly increasing if numbers[i] < numbers[i + 1] for all valid indices i.
An array of length 1 is already strictly increasing.

Examples:
Input: numbers = [1, 1, 1]
Output: 3

Input: numbers = [1, 5, 2, 4, 1]
Output: 14

Дан целочисленный массив numbers.
За одну операцию можно выбрать любой элемент массива и увеличить его на 1.

Нужно определить минимальное количество операций, чтобы сделать массив строго возрастающим.

Массив считается строго возрастающим, если для всех допустимых i выполняется numbers[i] < numbers[i + 1].
Массив длины 1 считается строго возрастающим автоматически.

Примеры:
Ввод: numbers = [1, 1, 1]
Вывод: 3

Ввод: numbers = [1, 5, 2, 4, 1]
Вывод: 14
'''

from typing import List

def min_operations(numbers: List[int]) -> int:
    operations_count = 0

    for index in range(1, len(numbers)):
        if numbers[index] <= numbers[index - 1]:
            required_value = numbers[index - 1] + 1
            increment_amount = required_value - numbers[index]
            operations_count += increment_amount
            numbers[index] = required_value

    return operations_count