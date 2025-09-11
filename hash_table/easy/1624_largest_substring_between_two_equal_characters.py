'''
Given a string S.

Return the length of the longest substring that lies between two equal characters, excluding those two characters themselves.

If no such substring exists, return -1.

A substring is a contiguous sequence of characters within a string.

Examples:
Input: S = "aa"
Output: 0

Input: S = "abca"
Output: 2

Дана строка S.

Нужно вернуть длину самой длинной подстроки, которая находится между двумя одинаковыми символами, не включая эти символы.

Если такой подстроки не существует, верните -1.

Подстрока — это непрерывная последовательность символов внутри строки.

Примеры:
Ввод: S = "aa"
Вывод: 0

Ввод: S = "abca"
Вывод: 2
'''

def max_length_between_equal_characters(S: str) -> int:
    first_occurrence = {}
    max_length = -1

    for i, character in enumerate(S):
        if character in first_occurrence:
            length = i - first_occurrence[character] - 1
            if length > max_length:
                max_length = length
        else:
            first_occurrence[character] = i

    return max_length