'''
The complement of an integer is formed by flipping all the 0's to 1's and all the 1's to 0's in its binary representation.
Given an integer number, return its complement.

Examples:
Input: number = 5
Output: 2

Input: number = 1
Output: 0

Дополнение числа — это число, полученное путём замены всех 0 на 1, а всех 1 на 0 в его двоичной записи.
Дан целое число number. Верните его дополнение.

Примеры:
Ввод: number = 5
Вывод: 2

Ввод: number = 1
Вывод: 0
'''

def find_complement(number: int) -> int:
    result = 0
    bit = 1

    while number > 0:
        if number % 2 == 0:
            result += bit
        number //= 2
        bit <<= 1
    return result