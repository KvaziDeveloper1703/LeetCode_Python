'''
Given an input string S and a pattern P, implement regular expression matching with support for the following:
    + '.' matches any single character;
    + '*' matches zero or more of the preceding element.

The matching should cover the entire input string.

Examples:
Input: S = "aa", P = "a"
Output: False

Input: S = "aa", P = "a*"
Output: True

Дана строка S и шаблон P, необходимо реализовать сопоставление с регулярным выражением, поддерживающее символы:
'.' — соответствует любому одному символу;
'*' — соответствует нулю или более предыдущих символов.

Сопоставление должно охватывать всю строку, а не её часть.

Примеры:
Ввод: S = "aa", P = "a"
Вывод: False

Ввод: S = "aa", P = "a*"
Вывод: True
'''

def is_match(S: str, P: str) -> bool:
    S_length, P_length = len(S), len(P)
    dp_table = [[False] * (P_length + 1) for _ in range(S_length + 1)]
    dp_table[0][0] = True

    for j in range(1, P_length + 1):
        if P[j - 1] == '*':
            dp_table[0][j] = dp_table[0][j - 2]

    for i in range(1, S_length + 1):
        for j in range(1, P_length + 1):
            if P[j - 1] == S[i - 1] or P[j - 1] == '.':
                dp_table[i][j] = dp_table[i - 1][j - 1]
            elif P[j - 1] == '*':
                dp_table[i][j] = dp_table[i][j - 2]
                if P[j - 2] == S[i - 1] or P[j - 2] == '.':
                    dp_table[i][j] = dp_table[i][j] or dp_table[i - 1][j]

    return dp_table[S_length][P_length]