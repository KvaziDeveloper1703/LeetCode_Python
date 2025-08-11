'''
Given a binary string S, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively. Count each substring as many times as it appears.

Examples:
Input: S = "00110011"
Output: 6

Input: S = "10101"
Output: 4

Дана двоичная строка S. Нужно вернуть количество непустых подстрок, в которых одинаковое количество 0 и 1, при этом все 0 и все 1 сгруппированы последовательно. Если такие подстроки встречаются несколько раз, каждая из них учитывается столько раз, сколько встречается.

Примеры:
Ввод: S = "00110011"
Вывод: 6

Ввод: S = "10101"
Вывод: 4
'''

def count_binary_substrings(S: str) -> int:
    groups = []
    count = 1

    for i in range(1, len(S)):
        if S[i] == S[i-1]:
            count += 1
        else:
            groups.append(count)
            count = 1
    groups.append(count)

    result = 0
    for i in range(1, len(groups)):
        result += min(groups[i-1], groups[i])

    return result