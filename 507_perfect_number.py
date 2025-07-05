'''
A perfect number is a positive integer that is equal to the sum of all its positive divisors, excluding itself.
A divisor of an integer x is a number that divides x evenly (without remainder).

Given an integer n, return true if n is a perfect number, otherwise return false.

Examples:
Input: number = 28
Output: true

Input: number = 7
Output: false

Совершенное число — это положительное целое число, которое равно сумме всех своих положительных делителей, не включая само число.
Делитель числа x — это число, которое делит x нацело (без остатка).

Дано целое число n. Верните true, если n является совершенным числом, и false в противном случае.

Примеры:
Ввод: number = 28
Вывод: true

Ввод: number = 7
Вывод: false
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