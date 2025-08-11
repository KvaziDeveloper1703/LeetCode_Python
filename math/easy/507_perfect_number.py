'''
A perfect number is a positive integer that is equal to the sum of all its positive divisors, excluding itself.
A divisor of an integer x is a number that divides x evenly.

Given an integer n, return True if n is a perfect number, otherwise return False.

Examples:
Input: number = 28
Output: True

Input: number = 7
Output: False

Совершенное число — это положительное целое число, которое равно сумме всех своих положительных делителей, не включая само число.
Делитель числа x — это число, которое делит x нацело.

Дано целое число n. Верните True, если n является совершенным числом, и False в противном случае.

Примеры:
Ввод: number = 28
Вывод: True

Ввод: number = 7
Вывод: False
'''

def check_perfect_number(self, number: int) -> bool:
    if number <= 1:
        return False

    total = 1
    i = 2

    while i * i <= number:
        if number % i == 0:
            total += i
            if i != number // i:
                total += number // i
        i += 1

    return total == number