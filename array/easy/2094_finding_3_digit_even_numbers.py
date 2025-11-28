'''
You are given an integer array digits, where each element represents a single digit. The array may contain duplicate values.

Your task is to find all unique integers that satisfy the following conditions:
    - The integer is formed by concatenating three elements from digits in any order;
    - The integer must not have a leading zero;
    - The integer must be even.

For example, if the digits are [1, 2, 3], the integers 132 and 312 satisfy the conditions.

Return a sorted array of all unique integers that meet the requirements.

Examples:
Input: digits = [2,1,3,0]
Output: [102,120,130,132,210,230,302,310,312,320]

Input: digits = [2,2,8,8,2]
Output: [222,228,282,288,822,828,882]

Вам дан массив целых чисел digits, где каждый элемент - это одна цифра. Массив может содержать повторяющиеся значения.

Нужно найти все уникальные целые числа, которые удовлетворяют следующим условиям:
    - Число составлено путём конкатенации трёх цифр из массива digits в любом порядке;
    - Число не должно начинаться с нуля;
    - Число должно быть чётным.

Например, если digits = [1, 2, 3], то числа 132 и 312 подходят под условия.

Верните отсортированный массив всех подходящих уникальных чисел.

Примеры:
Ввод: digits = [2,1,3,0]
Вывод: [102,120,130,132,210,230,302,310,312,320]

Ввод: digits = [2,2,8,8,2]
Вывод: [222,228,282,288,822,828,882]
'''

from typing import List

def find_even_numbers(digits: List[int]) -> List[int]:
    unique_numbers = set()

    length = len(digits)

    for i in range(length):
        for j in range(length):
            for k in range(length):
                if i == j or j == k or i == k:
                    continue

                first_digit = digits[i]
                second_digit = digits[j]
                third_digit = digits[k]

                if first_digit == 0:
                    continue

                if third_digit % 2 != 0:
                    continue

                number = first_digit * 100 + second_digit * 10 + third_digit
                unique_numbers.add(number)

    return sorted(unique_numbers)