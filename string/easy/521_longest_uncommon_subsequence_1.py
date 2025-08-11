'''
Given two strings a and b, return the length of the longest uncommon subsequence between them. If there is no such uncommon subsequence, return -1.
An uncommon subsequence is defined as a string that is a subsequence of exactly one of the two strings, but not both.

Examples:
Input: a = "aba", b = "cdc"
Output: 3

Input: a = "aaa", b = "bbb"
Output: 3

Даны две строки a и b. Необходимо вернуть длину самой длинной «необщей подпоследовательности» между ними. Если такой подпоследовательности не существует, верните -1.
Необщая подпоследовательность — это строка, которая является подпоследовательностью ровно одной из этих строк, но не обеих сразу.

Примеры:
Ввод: a = "aba", b = "cdc"
Вывод: 3

Ввод: a = "aaa", b = "bbb"
Вывод: 3
'''

def find_LUS_length(a: str, b: str) -> int:
    if a == b:
        return -1
    return max(len(a), len(b))