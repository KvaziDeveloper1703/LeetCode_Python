'''
You are given an array of positive integers numbers.

Your task is to determine whether it is possible to select two or more elements from the array such that the bitwise OR of the selected elements contains at least one trailing zero in its binary representation.

A trailing zero is a zero at the end of a binary number.

For example:
    - The binary representation of 5 is "101", which has no trailing zeros;
    - The binary representation of 4 is "100", which has two trailing zeros.

Return True if it is possible to choose two or more elements whose bitwise OR has at least one trailing zero. Return False otherwise.

Examples:
Input: numbers = [1,2,3,4,5]
Output: True

Input: numbers = [2,4,8,16]
Output: True

Дан массив положительных целых чисел numbers.

Необходимо определить, можно ли выбрать два или более элемента из массива так, чтобы их побитовое ИЛИ (bitwise OR) имело хотя бы один ноль в конце своей двоичной записи.

Концевой ноль - это ноль, находящийся в конце двоичного представления числа.

Например:
    - Двоичное представление числа 5 - "101", концевых нулей нет;
    - Двоичное представление числа 4 - "100", два концевых нуля.

Верните True, если существует выбор из двух или более элементов, для которых результат побитового ИЛИ содержит хотя бы один концевой ноль. Верните False в противном случае.

Примеры:
Ввод: numbers = [1,2,3,4,5]
Вывод: True

Ввод: numbers = [2,4,8,16]
Вывод: True
'''

from typing import List

def has_trailing_zeros(numbers: List[int]) -> bool:
    even_count = 0

    for number in numbers:
        if number % 2 == 0:
            even_count += 1
            if even_count >= 2:
                return True

    return False