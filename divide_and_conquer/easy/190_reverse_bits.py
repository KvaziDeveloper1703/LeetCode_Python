'''
Given a 32-bit unsigned integer n, return its bits reversed.
In some languages, there is no unsigned integer type. However, the underlying binary representation is the same for signed and unsigned integers. So treat the integer as a sequence of 32 bits and reverse the order of the bits.

Example:
Input: n = 00000010100101000001111010011100
Output: 964176192

Дано 32-битное беззнаковое целое число n. Требуется перевернуть порядок битов в этом числе и вернуть результат.
В некоторых языках программирования нет отдельного типа для беззнаковых целых чисел, но это не влияет на решение — внутреннее бинарное представление остаётся одинаковым для signed и unsigned типов.

Пример:
Ввод: n = 00000010100101000001111010011100
Вывод: 964176192 (в двоичной форме: 00111001011110000010100101000000)
'''

def reverse_bits(n: int) -> int:
    result = 0
    for _ in range(32):
        result <<= 1
        result |= n & 1
        n >>= 1
    return result