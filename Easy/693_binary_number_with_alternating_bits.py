'''
Given a positive integer n, check whether it has alternating bits: that is, whether any two adjacent bits in its binary representation always have different values.

Examples:
Input: n = 5
Output: True

Input: n = 7
Output: False

Дан положительный целое число n. Нужно проверить, имеет ли оно чередующиеся биты, то есть всегда ли два соседних бита в его двоичной записи имеют разные значения.

Примеры:
Ввод: n = 5
Вывод: True

Ввод: n = 7
Вывод: False
'''

def has_alternating_bits(n: int) -> bool:
    previous_bit = n & 1
    n >>= 1
    while n > 0:
        current_bit = n & 1
        if current_bit == previous_bit:
            return False
        previous_bit = current_bit
        n >>= 1
    return True