'''
You are given an integer array numbers.
For every element in numbers, replace it with the sum of its digits.
Return the minimum element in the array after all replacements.

Examples:
Input: numbers = [10, 12, 13, 14]
Output: 1

Input: numbers = [1, 2, 3, 4]
Output: 1

Вам дан целочисленный массив numbers.
Замените каждый элемент массива numbers на сумму его цифр.
Верните минимальный элемент массива после всех замен.

Примеры:
Ввод: numbers = [10, 12, 13, 14]
Вывод: 1

Ввод: numbers = [1, 2, 3, 4]
Вывод: 1
'''

from typing import List

def min_element(numbers: List[int]) -> int:
    def digit_sum(x: int) -> int:
        s = 0
        while x > 0:
            s += x % 10
            x //= 10
        return s

    answer = float("inf")

    for number in numbers:
        answer = min(answer, digit_sum(number))

    return answer