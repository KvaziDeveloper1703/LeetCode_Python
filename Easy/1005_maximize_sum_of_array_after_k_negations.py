'''
Given an integer array numbers and an integer k. You must perform the following operation exactly k times:
Choose any index i, and replace numbers[i] with -numbers[i].

Maximize the sum of the array after performing these k operations.
Return the maximum possible sum of the array.

Examples:
Input: numbers = [4, 2, 3], k = 1
Output: 5

Input: numbers = [3, -1, 0, 2], k = 3
Output: 6

Вам дан целочисленный массив numbers и целое число k. Вы должны выполнить следующую операцию ровно k раз:
Выберите любой индекс i и замените numbers[i] на -numbers[i].

Ваша цель — максимизировать сумму элементов массива после выполнения этих k операций.
Верните максимально возможную сумму массива.

Примеры:
Ввод: numbers = [4, 2, 3], k = 1
Вывод: 5

Ввод: numbers = [3, -1, 0, 2], k = 3
Вывод: 6
'''

from typing import List

def largest_sum_after_k_negations(numbers: List[int], k: int) -> int:
    numbers.sort()

    for i in range(len(numbers)):
        if k > 0 and numbers[i] < 0:
            numbers[i] = -numbers[i]
            k -= 1

    if k % 2 == 1:
        numbers.sort()
        numbers[0] = -numbers[0]

    return sum(numbers)