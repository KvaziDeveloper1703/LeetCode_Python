'''
You are given a string s consisting only of digits. You are allowed to perform at most one swap of two adjacent digits, but only if the two digits have the same parity.

Two digits have the same parity if:
    - both are even, or
    - both are odd.

Return the lexicographically smallest string that can be obtained after performing at most one such swap.

Examples:
Input: s = "45320"
Output: "43520"

Input: s = "001"
Output: "001"

Дана строка s, состоящая только из цифр. Разрешается выполнить не более одного обмена местами двух соседних цифр, но только если они имеют одинаковую чётность.

Две цифры имеют одинаковую чётность, если:
    - обе чётные, или
    - обе нечётные.

Верните лексикографически минимальную строку, которую можно получить после выполнения не более одного такого обмена.

Примеры:
Ввод: s = "45320"
Вывод: "43520"

Ввод: s = "001"
Вывод: "001"
'''

def get_smallest_string(s: str) -> str:
    digits = list(s)
    length = len(digits)

    for index in range(length - 1):
        leftDigit = int(digits[index])
        rightDigit = int(digits[index + 1])

        if (leftDigit % 2 == rightDigit % 2) and (digits[index] > digits[index + 1]):
            digits[index], digits[index + 1] = digits[index + 1], digits[index]
            return "".join(digits)

    return s