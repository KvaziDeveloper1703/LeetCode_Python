'''
You are given a string number consisting only of digits.
A digit string is called balanced if the sum of the digits at even indices is equal to the sum of the digits at odd indices.
Return true if the string number is balanced; otherwise, return false.

Examples:
Input: number = "1234"
Output: false

Input: number = "24123"
Output: true

Вам дана строка number, состоящая только из цифр.
Строка цифр называется сбалансированной, если сумма цифр на чётных индексах равна сумме цифр на нечётных индексах.
Необходимо вернуть true, если строка number является сбалансированной, и false - в противном случае.

Примеры:
Ввод: number = "1234"
Вывод: false

Ввод: number = "24123"
Вывод: true
'''

def is_balanced(number: str) -> bool:
    even_sum = 0
    odd_sum = 0

    for index, digit in enumerate(number):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    return even_sum == odd_sum