'''
A subsequence of a string is a sequence that can be formed by deleting some of the characters from the original string, without changing the order of the remaining characters.
Given two strings S and T, return True if S is a subsequence of T, and False otherwise.

Examples:
Input: S = "abc", T = "ahbgdc"
Output: True

Input: S = "axc", T = "ahbgdc"
Output: False

Подпоследовательность строки — это последовательность, которую можно получить, удалив некоторые символы из исходной строки, не меняя порядок оставшихся символов.
Даны две строки S и T. Верните True, если S является подпоследовательностью строки T, и False — в противном случае.

Примеры:
Ввод: S = "abc", T = "ahbgdc"
Вывод: True

Ввод: S = "axc", T = "ahbgdc"
Вывод: False
'''

def is_subsequence(S: str, T: str) -> bool:
    subsequence_index = 0
    target_index = 0

    while subsequence_index < len(S) and target_index < len(T):
        if S[subsequence_index] == T[target_index]:
            subsequence_index += 1
        target_index += 1

    return subsequence_index == len(S)