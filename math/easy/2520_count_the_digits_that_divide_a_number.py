'''
You are given an integer number.

Your task is to count how many digits of number divide the number itself.

A digit value is said to divide numbers if:
    - numbers % value == 0

Return the total number of such digits.

Examples:
Input: number = 7
Output: 1

Input: number = 121
Output: 2

Дано целое число number.

Необходимо определить, сколько цифр в числе number делят это число без остатка.

Цифра value считается делителем числа numbers, если:
    - numbers % value == 0

Верните количество таких цифр.

Примеры:
Ввод: number = 7
Вывод: 1

Ввод: number = 121
Вывод: 2
'''

def count_digits(numbers: int) -> int:
    count = 0
    original_number = numbers

    while numbers > 0:
        digit = numbers % 10
        if digit != 0 and original_number % digit == 0:
            count += 1
        numbers //= 10

    return count