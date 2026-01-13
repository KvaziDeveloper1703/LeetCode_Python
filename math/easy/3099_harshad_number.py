'''
An integer is called a Harshad number if it is divisible by the sum of its digits.
You are given an integer x. Return the sum of the digits of x if x is a Harshad number, otherwise return -1.

Examples:
Input: x = 18
Output: 9

Input: x = 23
Output: -1

Целое число называется числом Харшада, если оно делится на сумму своих цифр без остатка.
Дано целое число x. Верните сумму цифр числа x, если x - число Харшада, иначе верните -1.

Примеры:
Ввод: x = 18
Вывод: 9

Ввод: x = 23
Вывод: -1
'''

def sum_of_the_digits_of_harshad_number(x: int) -> int:
    digit_sum = sum(int(digit) for digit in str(x))

    if x % digit_sum == 0:
        return digit_sum

    return -1