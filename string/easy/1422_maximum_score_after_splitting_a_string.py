'''
Given a binary string S.

You need to split the string into two non-empty substrings — a left part and a right part.

The score of a split is defined as:
    + the number of '0' characters in the left substring plus;
    + the number of '1' characters in the right substring.

Return the maximum score possible from any valid split.

Examples:
Input: S = "011101"
Output: 5

Input:  S = "00111"
Output: 5

Дана двоичная строка S.

Нужно разделить строку на две непустые подстроки — левую и правую.

Оценка разделения вычисляется как:
    + количество символов '0' в левой подстроке плюс;
    + количество символов '1' в правой подстроке.

Нужно вернуть максимальную возможную оценку среди всех допустимых разделений.

Примеры:
Ввод: S = "011101"
Вывод: 5

Ввод: S = "00111"
Вывод: 5
'''

def max_score(S: str) -> int:
    total_ones = S.count('1')
    zeros_left = 0
    ones_seen = 0
    best = 0

    for i in range(len(S) - 1):
        if S[i] == '0':
            zeros_left += 1
        else:
            ones_seen += 1
        score = zeros_left + (total_ones - ones_seen)
        if score > best:
            best = score

    return best