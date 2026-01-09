'''
You are given a 0-indexed array of integers numbers.
A prefix numbers[0..i] is called sequential if for every index 1 ≤ j ≤ i, the following condition holds: numbers[j] = numbers[j - 1] + 1.
In particular, a prefix that consists of only numbers[0] is always considered sequential.
Your task is to find the smallest integer x that is missing from the array numbers, such that: x is greater than or equal to the sum of the longest sequential prefix of numbers.
Return this integer x.

Examples:
Input: numbers = [1,2,3,2,5]
Output: 6

Input: numbers = [3,4,5,1,12,14,13]
Output: 15

Дан целочисленный массив numbers с индексацией от 0.
Префикс numbers[0..i] называется последовательным, если для всех индексов 1 ≤ j ≤ i выполняется условие: numbers[j] = numbers[j - 1] + 1
В частности, префикс, состоящий только из элемента numbers[0], всегда считается последовательным.
Необходимо найти наименьшее целое число x, отсутствующее в массиве numbers, такое что: x больше либо равно сумме самого длинного последовательного префикса массива.
Верните это число x.

Примеры:
Ввод: numbers = [1,2,3,2,5]
Вывод: 6

Ввод: numbers = [3,4,5,1,12,14,13]
Вывод: 15
'''

from typing import List

def missing_integer(numbers: List[int]) -> int:
    prefix_sum = numbers[0]

    for index in range(1, len(numbers)):
        if numbers[index] == numbers[index - 1] + 1:
            prefix_sum += numbers[index]
        else:
            break

    numbers_set = set(numbers)
    current_number = prefix_sum

    while current_number in numbers_set:
        current_number += 1

    return current_number