'''
Given an integer n, return the difference between the product of its digits and the sum of its digits.

Examples:
Input: n = 234
Output: 15

Input: n = 4421
Output: 21

Дано целое число n. Верните разницу между произведением его цифр и суммой его цифр.

Примеры:
Ввод: n = 234
Вывод: 15

Ввод: n = 4421
Вывод: 21
'''

def subtract_product_and_sum(n: int) -> int:
    product = 1
    total_sum = 0
    for digit in str(n):
        d = int(digit)
        product *= d
        total_sum += d
    return product - total_sum