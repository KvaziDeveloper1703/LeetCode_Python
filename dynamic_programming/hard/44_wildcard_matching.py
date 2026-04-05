'''
Given an input string S and a pattern P, implement wildcard pattern matching with support for:
    + ? matches any single character;
    + * matches any sequence of characters.

The match must cover the entire input string, not just part of it.

Example:
Input: S = "aa", P = "a"
Output: False

Дана входная строка S и шаблон P, реализуйте сопоставление с шаблоном, поддерживающим следующие символы:
    + ? — соответствует одному любому символу;
    + * — соответствует любому количеству любых символов, включая ноль символов.

Сопоставление должно охватывать всю строку S, а не её часть.

Пример:
Ввод: S = "aa", P = "a"
Вывод: False
'''

def is_match(S: str, P: str) -> bool:
    S_length = len(S)
    P_length = len(P)

    dp_table = [[False] * (P_length + 1) for _ in range(S_length + 1)]
    dp_table[0][0] = True

    for P_index in range(1, P_length + 1):
        if P[P_index - 1] == '*':
            dp_table[0][P_index] = dp_table[0][P_index - 1]

    for S_index in range(1, S_length + 1):
        for P_index in range(1, P_length + 1):
            current_S_char = S[S_index - 1]
            current_P_char = P[P_index - 1]

            if current_P_char == current_S_char or current_P_char == '?':
                dp_table[S_index][P_index] = dp_table[S_index - 1][P_index - 1]
            elif current_P_char == '*':
                match_zero = dp_table[S_index][P_index - 1]
                match_more = dp_table[S_index - 1][P_index]
                dp_table[S_index][P_index] = match_zero or match_more

    return dp_table[S_length][P_length]