'''
You are given three strings: s1, s2, and s3.

In one operation, you may choose one of the strings and delete its rightmost character.

Note that a string cannot be completely emptied - at least one character must remain.

Your task is to determine the minimum number of operations required to make all three strings equal.

If it is impossible to make the strings equal, return -1.

Examples:
Input: s1 = "abc", s2 = "abb", s3 = "ab"
Output: 2

Input: s1 = "dac", s2 = "bac", s3 = "cac"
Output: -1

Даны три строки: s1, s2 и s3.

За одну операцию можно выбрать одну из строк и удалить её последний (правый) символ.

При этом нельзя полностью удалить строку - в ней должен остаться хотя бы один символ.

Необходимо определить минимальное количество операций, требуемое для того, чтобы все три строки стали одинаковыми.

Если сделать строки одинаковыми невозможно, нужно вернуть -1.

Примеры:
Ввод: s1 = "abc", s2 = "abb", s3 = "ab"
Вывод: 2

Ввод: s1 = "dac", s2 = "bac", s3 = "cac"
Вывод: -1
'''

def find_minimum_operations(s1: str, s2: str, s3: str) -> int:
    minimum_length = min(len(s1), len(s2), len(s3))
    common_prefix_length = 0

    for index in range(minimum_length):
        if s1[index] == s2[index] == s3[index]:
            common_prefix_length += 1
        else:
            break

    if common_prefix_length == 0:
        return -1

    operations_count = (
        len(s1) - common_prefix_length +
        len(s2) - common_prefix_length +
        len(s3) - common_prefix_length
    )

    return operations_count