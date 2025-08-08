'''
Given a list of integers numbers that represents a run-length encoded list.
Each adjacent pair of elements [freq, value] = [numbers[2*i], numbers[2*i+1]] means that value appears freq times.

Decompress the list by expanding each [freq, value] pair into freq copies of value, and concatenate all of them in order from left to right.
Return the resulting decompressed list.

Examples:
Input: numbers = [1, 2, 3, 4]
Output: [2, 4, 4, 4]

Input: numbers = [1, 1, 2, 3]
Output: [1, 3, 3]

Дан список целых чисел numbers, закодированный с использованием кодирования с длиной серии.
Каждая пара подряд идущих элементов [freq, value] = [numbers[2*i], numbers[2*i+1]] означает, что число value повторяется freq раз. То есть пара [3, 4] означает [4, 4, 4].

Нужно декодировать список, то есть:
    + Для каждой пары [freq, value] создать подсписок, содержащий freq копий value;
    + Объединить все подсписки слева направо и вернуть полученный список.

Примеры:
Ввод: numbers = [1, 2, 3, 4]
Вывод: [2, 4, 4, 4]

Ввод: numbers = [1, 1, 2, 3]
Вывод: [1, 3, 3]
'''

from typing import List

def decompress_RLE_list(numbers: List[int]) -> List[int]:
    result = []
    for i in range(0, len(numbers), 2):
        freq = numbers[i]
        value = numbers[i + 1]
        result.extend([value] * freq)
    return result