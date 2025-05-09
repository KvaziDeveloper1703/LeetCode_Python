'''
You are given three strings: s1, s2, and s3. Your task is to determine whether s3 can be formed by interleaving s1 and s2.

Definition – Interleaving of two strings:
An interleaving of strings s and t means they are split into substrings like:
+ s = s1 + s2 + ... + sn
+ t = t1 + t2 + ... + tm

With the condition |n - m| <= 1, and the substrings are interleaved in alternating order, for example:
+ s1 + t1 + s2 + t2 + s3 + t3 + ... or
+ t1 + s1 + t2 + s2 + t3 + s3 + ...

That is, the order of characters in each original string must be preserved.
Return true if s3 is a valid interleaving of s1 and s2, otherwise return false.

Example:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Даны три строки: s1, s2 и s3. Необходимо определить, можно ли сформировать строку s3 путём чередования символов строк s1 и s2.

Что такое чередование строк:

Строки s1 и s2 разбиваются на подпоследовательности:
+ s1 = s1₁ + s1₂ + ... + s1ₙ
+ s2 = s2₁ + s2₂ + ... + s2ₘ
+ с условием |n - m| <= 1

И объединяются в чередующемся порядке:
+ s1₁ + s2₁ + s1₂ + s2₂ + ... или s2₁ + s1₁ + s2₂ + s1₂ + ...

При этом порядок символов в s1 и s2 должен сохраняться.
Нужно вернуть true, если s3 можно получить таким образом, иначе — false.

Пример:
Ввод: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Вывод: true
'''

def is_inter_leave(s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False

    is_valid_interleave = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    is_valid_interleave[0][0] = True

    for i in range(1, len(s1) + 1):
        is_valid_interleave[i][0] = (
            is_valid_interleave[i - 1][0] and s1[i - 1] == s3[i - 1]
        )

    for j in range(1, len(s2) + 1):
        is_valid_interleave[0][j] = (
            is_valid_interleave[0][j - 1] and s2[j - 1] == s3[j - 1]
        )

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            is_valid_interleave[i][j] = (
                (is_valid_interleave[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or
                (is_valid_interleave[i][j - 1] and s2[j - 1] == s3[i + j - 1])
            )

    return is_valid_interleave[len(s1)][len(s2)]