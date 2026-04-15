'''
We can scramble a string s to get another string t using the following algorithm:
    - If the length of the string is 1, stop;
    - If the length of the string is greater than 1, do the following:
        - Split the string into two non-empty substrings at a random index. That is, if s, then divide it into x and y such that: s = x + y;
        - Randomly decide whether to swap the two substrings or keep them in the same order: s = x + y or s = y + x;
        - Apply the same process recursively to both substrings x and y.

Given two strings s1 and s2 of the same length, return:
    - true if s2 is a scrambled string of s1;
    - false otherwise.

Examples:
Input: s1 = "great", s2 = "rgeat"
Output: true

Input: s1 = "abcde", s2 = "caebd"
Output: false

Мы можем перемешать строку s, чтобы получить строку t, используя следующий алгоритм:
    - Если длина строки равна 1, остановиться;
    - Если длина строки больше 1, выполнить:
        - Разделить строку на две непустые подстроки в случайной позиции. То есть представить s как: s = x + y;
        - Случайно решить: оставить порядок (x + y) или поменять части местами (y + x);
        - Рекурсивно применить тот же алгоритм к подстрокам x и y.

Даны две строки s1 и s2 одинаковой длины. Нужно вернуть:
    - true, если s2 является перемешанной версией строки s1;
    - false в противном случае.

Примеры:
Ввод: s1 = "great", s2 = "rgeat"
Вывод: true

Ввод: s1 = "abcde", s2 = "caebd"
Вывод: false
'''

def is_scramble(s1: str, s2: str) -> bool:
    memo = {}

    def dfs(a, b):
        if (a, b) in memo:
            return memo[(a, b)]

        if a == b:
            memo[(a, b)] = True
            return True

        if sorted(a) != sorted(b):
            memo[(a, b)] = False
            return False

        n = len(a)

        for i in range(1, n):
            if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                memo[(a, b)] = True
                return True

            if dfs(a[:i], b[n-i:]) and dfs(a[i:], b[:n-i]):
                memo[(a, b)] = True
                return True

        memo[(a, b)] = False
        return False

    return dfs(s1, s2)