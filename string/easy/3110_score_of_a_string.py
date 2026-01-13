'''
You are given a string s.
The score of a string is defined as the sum of the absolute differences between the ASCII values of adjacent characters.
Return the score of s.

Examples:
Input: s = "hello"
Output: 13

Input: s = "zaz"
Output: 50

Дана строка s.
Счёт строки определяется как сумма модулей разностей ASCII-кодов соседних символов.
Нужно вернуть score строки s.

Примеры:
Ввод: s = "hello"
Вывод: 13

Ввод: s = "zaz"
Вывод: 50
'''

def score_of_string(s: str) -> int:
    total_score = 0

    for index in range(1, len(s)):
        total_score += abs(ord(s[index]) - ord(s[index - 1]))

    return total_score