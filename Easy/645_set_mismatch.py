'''
You have a set of integers s that originally contains all the numbers from 1 to n.
Unfortunately, due to an error, one of the numbers in s got duplicated, which caused one number to appear twice and another number to be missing.

You are given an integer array numbers representing the current state of this set after the error.

Your task is to find:
    + the number that occurs twice, and
    + the number that is missing.

Return them as an array: [duplicate, missing].

Examples:
Input: numbers = [1,2,2,4]
Output: [2,3]

Input: numbers = [1,1]
Output: [1,2]

Есть множество целых чисел s, которое изначально содержало все числа от 1 до n.
К сожалению, из-за ошибки одно из чисел было продублировано, что привело к тому, что одно число появилось дважды, а другое оказалось отсутствующим.

Дан массив целых чисел nums, представляющий текущее состояние этого множества после ошибки.

Ваша задача — найти:
    + число, которое встречается дважды, и
    + число, которое отсутствует.

Верните их в виде массива: [дублирующееся число, отсутствующее число].

Примеры:
Ввод: numbers = [1,2,2,4]
Вывод: [2,3]

Ввод: numbers = [1,1]
Вывод: [1,2]
'''

from typing import List

def find_error_numbers(numbers: List[int]) -> List[int]:
    n = len(numbers)
    seen = set()
    duplicate = -1

    for number in numbers:
        if number in seen:
            duplicate = number
        seen.add(number)

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)

    missing = expected_sum - (actual_sum - duplicate)

    return [duplicate, missing]