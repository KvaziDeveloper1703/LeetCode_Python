'''
A balanced string is a string in which the number of characters 'L' is equal to the number of characters 'R'.

Given a balanced string S. Split it into the maximum possible number of substrings such that:
    + Each substring is itself balanced;
    + Return the maximum number of such balanced substrings.

Examples:
Input: S = "RLRRLLRLRL"
Output: 4

Input: S = "RLRRRLLRLL"
Output: 2

Сбалансированная строка — это строка, в которой количество символов 'L' равно количеству символов 'R'.

Дана сбалансированная строка S. Разбейте её на максимальное количество подстрок так, чтобы:
    + Каждая подстрока была сбалансированной;
    + Вернуть максимальное количество таких подстрок.

Примеры:
Ввод: S = "RLRRLLRLRL"
Вывод: 4

Ввод: S = "RLRRRLLRLL"
Вывод: 2
'''

def balanced_string_split(S: str) -> int:
    count = 0
    balance = 0

    for character in S:
        if character == 'L':
            balance += 1
        else:
            balance -= 1

        if balance == 0:
            count += 1

    return count