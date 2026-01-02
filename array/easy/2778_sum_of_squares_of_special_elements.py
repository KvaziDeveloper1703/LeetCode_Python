'''
You are given a 1-indexed integer array numbers of length n.

An element numbers[i] is called special if the index i divides n, that is: n % i == 0.

Your task is to return the sum of the squares of all special elements in the array.

Examples:
Input: numbers = [1, 2, 3, 4]
Output: 21

Input: numbers = [2, 7, 1, 19, 18, 3]
Output: 63

Вам дан 1-индексированный массив целых чисел numbers длины n.

Элемент numbers[i] называется специальным, если индекс i делит n без остатка, то есть: n % i == 0.

Необходимо вернуть сумму квадратов всех специальных элементов массива.

Примеры:
Ввод: numbers = [1, 2, 3, 4]
Вывод: 21

Ввод: numbers = [2, 7, 1, 19, 18, 3]
Вывод: 63
'''

from typing import List

def sum_of_squares(numbers: List[int]) -> int:
    n = len(numbers)
    result = 0

    for i in range(1, n + 1):
        if n % i == 0:
            result += numbers[i - 1] ** 2

    return result