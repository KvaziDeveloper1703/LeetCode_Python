'''
Given a binary array bits that ends with a 0.

There are two types of characters in this encoding:
    + A one-bit character is represented by a single bit 0;
    + A two-bit character is represented by either 10 or 11.

Determine whether the last character in the array must be a one-bit character.

Return True if the last character is definitely a one-bit character, otherwise return False.

Examples:
Input: bits = [1, 0, 0]
Output: True

Input: bits = [1, 1, 1, 0]
Output: False

Дан бинарный массив bits, который заканчивается нулём.

В системе кодирования используются два типа символов:
    + Однобитный символ кодируется как 0;
    + Двухбитный символ кодируется как 10 или 11.

Необходимо определить, является ли последний символ в массиве однобитным.

Верните True, если последний символ обязательно однобитный, иначе верните False.

Примеры:
Ввод: bits = [1, 0, 0]
Вывод: True

Ввод: bits = [1, 1, 1, 0]
Вывод: False
'''

from typing import List

def is_one_bit_character(bits: List[int]) -> bool:
    i = 0
    n = len(bits)
    while i < n - 1:
        if bits[i] == 1:
            i += 2
        else:
            i += 1
    return i == n - 1