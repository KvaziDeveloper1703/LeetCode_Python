'''
You are given two binary strings a and b.
Return their sum as a binary string.

Examples:
Input: a = "11", b = "1"
Output: "100"

Даны две двоичные строки a и b.
Верните их сумму в виде двоичной строки.

Примеры:
Ввод: a = "11", b = "1"
Вывод: "100"
'''

def add_binary(first_binary: str, second_binary: str) -> str:
    result = []
    carry = 0

    index_first = len(first_binary) - 1
    index_second = len(second_binary) - 1

    while index_first >= 0 or index_second >= 0 or carry:
        bit1 = int(first_binary[index_first]) if index_first >= 0 else 0
        bit2 = int(second_binary[index_second]) if index_second >= 0 else 0
        total = bit1 + bit2 + carry
        carry = total // 2
        result.append(str(total % 2))
        index_first -= 1
        index_second -= 1

    result.reverse()
    return ''.join(result)