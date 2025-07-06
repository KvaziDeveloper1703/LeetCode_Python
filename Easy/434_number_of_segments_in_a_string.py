'''
Given a string S, return the number of segments in the string.
A segment is defined as a contiguous sequence of non-space characters.

Examples:
Input: S = "Hello, my name is John"
Output: 5

Input: S = "Hello"
Output: 1

Дана строка S. Верните количество сегментов в этой строке.
Сегментом считается непрерывная последовательность символов, отличных от пробела.

Примеры:
Ввод: S = "Hello, my name is John"
Вывод: 5

Ввод: S = "Hello"
Вывод: 1
'''

def count_segments(S: str) -> int:
    return len(S.split())