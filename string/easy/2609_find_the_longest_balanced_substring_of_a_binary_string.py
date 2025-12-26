'''
You are given a binary string s consisting only of characters '0' and '1'.

A substring of s is called balanced if:
    - all '0' characters appear before any '1' characters, and
    - the number of '0' characters is equal to the number of '1' characters in the substring.

Return the length of the longest balanced substring of s.

Examples:
Input: s = "01000111"
Output: 6

Input: s = "00111"
Output: 4

Дана двоичная строка s, состоящая только из символов '0' и '1'.

Подстрока строки s называется сбалансированной, если:
    - все символы '0' идут перед символами '1', и
    - количество символов '0' равно количеству символов '1' в подстроке.

Необходимо вернуть длину самой длинной сбалансированной подстроки строки s.

Примеры:
Ввод: s = "01000111"
Вывод: 6

Ввод: s = "00111"
Вывод: 4
'''

def find_the_longest_balanced_substring(s: str) -> int:
    maximum_length = 0
    current_zeros = 0
    current_ones = 0

    for character in s:
        if character == '0':
            if current_ones > 0:
                current_zeros = 0
                current_ones = 0
            current_zeros += 1
        else:
            current_ones += 1
            maximum_length = max(maximum_length, 2 * min(current_zeros, current_ones))

    return maximum_length