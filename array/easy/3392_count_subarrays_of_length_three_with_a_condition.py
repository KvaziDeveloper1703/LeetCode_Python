'''
You are given an integer array numbers.
Your task is to determine how many subarrays of length 3 satisfy the following condition: The sum of the first and third elements of the subarray is exactly equal to half of the second (middle) element.
Return the number of such subarrays.

Examples:
Input: numbers = [1, 2, 1, 4, 1]
Output: 1

Input: numbers = [1, 1, 1]
Output: 0

Дан массив целых чисел numbers.
Нужно определить количество подмассивов длины 3, которые удовлетворяют следующему условию: Сумма первого и третьего элементов подмассива равна половине второго (среднего) элемента.
Верните количество таких подмассивов.

Примеры:
Ввод: numbers = [1, 2, 1, 4, 1]
Вывод: 1

Ввод: numbers = [1, 1, 1]
Вывод: 0
'''

from typing import List

def count_subarrays(numbers: List[int]) -> int:
    total_count = 0

    for index in range(len(numbers) - 2):
        first_value = numbers[index]
        middle_value = numbers[index + 1]
        third_value = numbers[index + 2]

        if 2 * (first_value + third_value) == middle_value:
            total_count += 1

    return total_count