'''
You are given a string s consisting only of the characters 'a' and 'b'.
In one step, you can remove any palindromic subsequence from the string.
Your task is to return the minimum number of steps required to make the string empty.

Examples:
Input: s = "ababa"
Output: 1

Input: s = "abb"
Output: 2

Дана строка s, состоящая только из символов 'a' и 'b'.
За один шаг можно удалить любую палиндромную подпоследовательность строки.
Необходимо определить минимальное количество шагов, чтобы полностью удалить строку.

Примеры:
Ввод: s = "ababa"
Вывод: 1

Ввод: s = "abb"
Вывод: 2
'''

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        if s == s[::-1]:
            return 1
        return 2