'''
Given two strings S and goal, return True if and only if S can become goal after some number of shifts on S.

A shift on S consists of moving the leftmost character of S to the rightmost position.

Examples:
Input: S = "abcde", goal = "cdeab"
Output: True

Input: S = "abcde", goal = "abced"
Output: False

Даны две строки S и goal. Верните True только в том случае, если из строки S можно получить goal после некоторого количества сдвигов.

Сдвиг строки — это операция, при которой первый символ перемещается в конец строки.

Примеры:
Ввод: S = "abcde", goal = "cdeab"
Вывод: True

Ввод: S = "abcde", goal = "abced"
Вывод: False
'''

def rotate_string(S: str, goal: str) -> bool:
    if len(S) != len(goal):
        return False
    return goal in (S + S)