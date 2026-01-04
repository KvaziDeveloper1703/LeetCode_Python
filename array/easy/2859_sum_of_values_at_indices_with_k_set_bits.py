'''
You are given a 0-indexed integer array numbers and an integer k.

Return an integer representing the sum of the elements in numbers whose indices contain exactly k set bits in their binary representation.

A set bit is a 1 in the binary form of a number.

Examples:
Input: numbers = [5,10,1,5,2], k = 1
Output: 13

Input: numbers = [4,3,2,1], k = 2
Output: 1

Вам дан массив целых чисел с нумерацией от нуля numbers и целое число k.

Необходимо вернуть сумму элементов массива numbers, индексы которых содержат ровно k установленных битов (1) в их двоичном представлении.

Установленные биты (set bits) - это единицы (1) в двоичной записи числа.

Примеры:
Ввод: numbers = [5,10,1,5,2], k = 1
Вывод: 13

Ввод: numbers = [4,3,2,1], k = 2
Вывод: 1
'''

from typing import List

def sum_indices_with_k_set_bits(numbers: List[int], k: int) -> int:
    total_sum = 0

    for index, value in enumerate(numbers):
        if bin(index).count("1") == k:
            total_sum += value

    return total_sum