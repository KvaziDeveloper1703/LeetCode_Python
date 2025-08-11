'''
Given an integer array numbers, rearrange the elements so that all even integers come before all the odd integers.

Return any array that satisfies this condition. The order of even and odd numbers within their groups does not matter.

Examples:
Input: numbers = [3, 1, 2, 4]
Output: [2, 4, 3, 1]

Input: numbers = [0]
Output: [0]

Дан массив целых чисел numbers. Необходимо переставить элементы так, чтобы все чётные числа шли в начале массива, а все нечётные — в конце.

Верните любой массив, удовлетворяющий этому условию. Порядок следования чётных и нечётных чисел внутри своих групп не важен.

Примеры:
Ввод: numbers = [3, 1, 2, 4]
Вывод: [2, 4, 3, 1]

Ввод: numbers = [0]
Вывод: [0]
'''

from typing import List

def sort_array_by_parity(numbers: List[int]) -> List[int]:
    even_numbers = []
    odd_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    return even_numbers + odd_numbers