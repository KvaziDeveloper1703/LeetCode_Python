'''
You are given an integer array numbers that does not contain any zeros.

Your task is to find the largest positive integer k such that both k and -k are present in the array.

Return the value of k.

If no such integer exists, return -1.

Examples:
Input: numbers = [-1, 2, -3, 3]
Output: 3

Input: numbers = [-1, 10, 6, 7, -7, 1]
Output: 7

Дан массив целых чисел numbers, который не содержит нулей.

Необходимо найти наибольшее положительное целое число k, такое что и число k, и число -k присутствуют в массиве.

Верните значение k.

Если такого числа не существует, верните -1.

Примеры:
Ввод: numbers = [-1, 2, -3, 3]
Вывод: 3

Ввод: numbers = [-1, 10, 6, 7, -7, 1]
Вывод: 7
'''

from typing import List

def find_max_k(numbers: List[int]) -> int:
    numbers_set = set(numbers)
    maximum_k = -1

    for number in numbers_set:
        if number > 0 and -number in numbers_set:
            if number > maximum_k:
                maximum_k = number

    return maximum_k