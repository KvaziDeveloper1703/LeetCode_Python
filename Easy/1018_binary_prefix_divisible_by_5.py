'''
Given a binary array numbers.

We define xi as the integer whose binary representation is the subarray numbers[0..i].

For example, if numbers = [1,0,1], then:
    + x0 = 1 (binary "1")
    + x1 = 2 (binary "10")
    + x2 = 5 (binary "101")

Return a boolean array answer where answer[i] is True if xi is divisible by 5, and False otherwise.

Examples:
Input: numbers = [0, 1, 1]
Output: [True, False, False]

Input: numbers = [1, 1, 1]
Output: [False, False, False]

Вам дан двоичный массив numbers.

Определим xi как число, двоичное представление которого состоит из подмассива numbers[0..i].

Например, если numbers = [1,0,1], то:
    + x0 = 1 (в двоичной системе "1")
    + x1 = 2 (в двоичной системе "10")
    + x2 = 5 (в двоичной системе "101")

Верните булев массив answer, где answer[i] равно True, если xi делится на 5, и False — в противном случае.

Примеры:
Ввод: numbers = [0, 1, 1]
Вывод: [True, False, False]

Ввод: numbers = [1, 1, 1]
Вывод: [False, False, False]
'''

from typing import List

def prefixes_divisible_by_5(numbers: List[int]) -> List[bool]:
    result = []
    number = 0

    for bit in numbers:
        number = (number * 2 + bit) % 5
        result.append(number == 0)

    return result