'''
Given an integer numbers, repeatedly add all of its digits until the result contains only one digit, then return that digit.

Examples:
Input: numbers = 38
Output: 2

Input: numbers = 0
Output: 0

Дано целое число numbers. Нужно многократно складывать все его цифры, пока результат не станет однозначным числом, и вернуть этот результат.

Примеры:
Ввод: numbers = 38
Вывод: 2

Ввод: numbers = 0
Вывод: 0
'''

def add_digits(numbers: int) -> int:
    while numbers >= 10:
        digits_sum = 0

        while numbers > 0:
            digits_sum += numbers % 10
            numbers //= 10

        numbers = digits_sum

    return numbers