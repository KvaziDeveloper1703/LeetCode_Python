'''
A self-dividing number is a number that is divisible by each of its digits.
For example, 128 is a self-dividing number because: 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
A self-dividing number cannot contain the digit 0, since division by zero is undefined.

Given two integers left and right, return a list of all self-dividing numbers in the range [left, right].

Examples:
Input: left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

Input: left = 47, right = 85
Output: [48, 55, 66, 77]

Самоделящиеся числа — это числа, которые делятся на каждую из своих цифр без остатка.
Например, 128 — это самоделящееся число, потому что: 128 % 1 == 0, 128 % 2 == 0, и 128 % 8 == 0.
Самоделящиеся числа не могут содержать цифру 0, так как деление на ноль невозможно.

Даны два целых числа left и right. Верните список всех самоделящихся чисел в диапазоне [left, right], включая границы.

Примеры:
Ввод: left = 1, right = 22
Вывод: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

Ввод: left = 47, right = 85
Вывод: [48, 55, 66, 77]
'''

from typing import List

def self_dividing_numbers(self, left: int, right: int) -> List[int]:
    def is_self_dividing(n: int) -> bool:
        for digit in str(n):
            if digit == '0' or n % int(digit) != 0:
                return False
        return True

    result = []
    for number in range(left, right + 1):
        if is_self_dividing(number):
            result.append(number)
    return result