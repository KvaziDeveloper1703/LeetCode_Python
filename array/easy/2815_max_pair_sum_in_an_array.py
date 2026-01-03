'''
You are given an array of integers numbers.

For each number, define its largest digit as the maximum digit appearing in its decimal representation. For example, the number 2373 consists of the digits 2, 3, and 7, and its largest digit is 7.

Your task is to find two different numbers in the array such that their largest digits are equal, and the sum of these two numbers is maximized.

Return the maximum possible sum of such a pair. If no such pair exists, return -1.

Examples:
Input: numbers = [112, 131, 411]
Output: -1

Input: numbers = [2536, 1613, 3366, 162]
Output: 5902

Дан массив целых чисел numbers.

Для каждого числа определим его наибольшую цифру - это максимальная цифра в его десятичной записи. Например, число 2373 состоит из цифр 2, 3 и 7, где наибольшей является 7.

Необходимо найти два различных числа в массиве, у которых наибольшая цифра одинакова, и сумма этих чисел максимальна.

Верните максимальную возможную сумму такой пары. Если подходящей пары не существует, верните -1.

Примеры:
Ввод: numbers = [112, 131, 411]
Вывод: -1

Ввод: numbers = [2536, 1613, 3366, 162]
Вывод: 5902
'''

from typing import List
from collections import defaultdict

def max_sum(numbers: List[int]) -> int:
    groups = defaultdict(list)

    for number in numbers:
        max_digit = max(map(int, str(number)))
        groups[max_digit].append(number)

    result = -1

    for values in groups.values():
        if len(values) >= 2:
            values.sort(reverse=True)
            result = max(result, values[0] + values[1])

    return result