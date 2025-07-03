'''
The complement of an integer is formed by flipping all the 0's to 1's and all the 1's to 0's in its binary representation (ignoring leading zero bits).
Given an integer num, return its complement.

Examples:
Input: num = 5
Output: 2

Input: num = 1
Output: 0

Дополнение числа — это число, полученное путём замены всех 0 на 1, а всех 1 на 0 в его двоичной записи (без учёта ведущих нулей).
Дан целое число num. Верните его дополнение.

Примеры:
Ввод: num = 5
Вывод: 2

Ввод: num = 1
Вывод: 0
'''

class Solution:
    def findComplement(self, num: int) -> int:
        result = 0
        bit = 1
        while num > 0:
            if num % 2 == 0:
                result += bit
            num //= 2
            bit <<= 1
        return result