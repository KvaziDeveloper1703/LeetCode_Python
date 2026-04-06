'''
You are given two binary strings first_binary and second_binary.
Return their sum as a binary string.

Examples:
Input: first_binary = "11", second_binary = "1"
Output: "100"

Даны две двоичные строки first_binary и second_binary.
Верните их сумму в виде двоичной строки.

Примеры:
Ввод: first_binary = "11", second_binary = "1"
Вывод: "100"
'''

def add_binary(first_binary: str, second_binary: str) -> str:
    result = []
    carry = 0

    index_first = len(first_binary) - 1
    index_second = len(second_binary) - 1

    while index_first >= 0 or index_second >= 0 or carry:
        bit_1 = int(first_binary[index_first]) if index_first >= 0 else 0
        bit_2 = int(second_binary[index_second]) if index_second >= 0 else 0
        total = bit_1 + bit_2 + carry
        carry = total // 2
        result.append(str(total % 2))
        index_first -= 1
        index_second -= 1

    result.reverse()
    return ''.join(result)