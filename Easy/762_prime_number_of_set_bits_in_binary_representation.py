'''
Given two integers left and right, return the count of numbers in the inclusive range [left, right] that have a prime number of set bits in their binary representation.
A set bit is a 1 in the binary form of a number.

Examples:
Input: left = 6, right = 10
Output: 4

Input: left = 10, right = 15
Output: 5

Даны два целых числа left и right. Верните количество чисел в включительном диапазоне [left, right], у которых простое количество установленных битов в двоичном представлении.
Установленный бит — это 1 в двоичной записи числа.

Примеры:
Ввод: left = 6, right = 10
Вывод: 4

Ввод: left = 10, right = 15
Вывод: 5
'''

def count_prime_set_bits(left: int, right: int) -> int:
    primes = {2, 3, 5, 7, 11, 13, 17, 19}

    def count_set_bits(n):
        return bin(n).count('1')

    count = 0
    for number in range(left, right + 1):
        if count_set_bits(number) in primes:
            count += 1
    return count