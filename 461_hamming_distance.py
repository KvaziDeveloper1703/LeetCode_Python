'''
The Hamming distance between two integers is the number of bit positions at which the corresponding bits are different.
Given two integers x and y, return the Hamming distance between them.

Examples:
Input: x = 1, y = 4
Output: 2

Input: x = 3, y = 1
Output: 1

Хэммингова дистанция между двумя целыми числами — это количество позиций, в которых соответствующие биты различаются.
Даны два целых числа x и y. Верните расстояние Хэмминга между ними.

Примеры:
Ввод: x = 1, y = 4
Вывод: 2

Ввод: x = 3, y = 1
Вывод: 1
'''

def hamming_distance(x: int, y: int) -> int:
    difference = x ^ y
    return bin(difference).count('1')