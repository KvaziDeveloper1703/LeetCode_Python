'''
Given a positive integer n, write a function that returns the number of set bits (1s) in its binary representation.
This is also known as the Hamming weight of the number.

Example:
Input: n = 11
Output: 3

Дано положительное целое число n. Напишите функцию, которая возвращает количество установленных битов (единиц) в его двоичном представлении.
Это также называется вес Хэмминга числа.

Пример:
Ввод: n = 11
Вывод: 3
'''

def hamming_weight(n: int) -> int:
    binary = bin(n)
    count = 0
    for digit in binary:
        if digit == '1':
            count += 1
    return count