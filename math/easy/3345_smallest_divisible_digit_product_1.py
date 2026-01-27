'''
You are given two integers n and t.

Your task is to find and return the smallest integer that is greater than or equal to n such that the product of its digits is divisible by t.

Examples:
Input: n = 10, t = 2
Output: 10

Input: n = 15, t = 3
Output: 16

Вам даны два целых числа n и t.

Необходимо найти и вернуть наименьшее число, которое больше или равно n, такое, что произведение его цифр делится на t.

Примеры:
Ввод: n = 10, t = 2
Вывод: 10

Ввод: n = 15, t = 3
Вывод: 16
'''

def smallest_number(n: int, t: int) -> int:
    current = n

    while True:
        product = 1
        for digit in str(current):
            product *= int(digit)

        if product % t == 0:
            return current

        current += 1