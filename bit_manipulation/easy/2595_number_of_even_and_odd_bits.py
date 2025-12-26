'''
You are given a positive integer n.

Define:
    - even - the number of bits equal to 1 at even indices in the binary representation of n;
    - odd - the number of bits equal to 1 at odd indices in the binary representation of n.

Bits are indexed from right to left, starting with index 0.

Return an array [even, odd].

Examples:
Input: n = 50
Output: [1, 2]

Input: n = 2
Output: [0, 1]

Дано положительное целое число n.

Определим:
    - even - количество битов, равных 1, находящихся на чётных позициях в двоичном представлении числа n;
    - odd - количество битов, равных 1, находящихся на нечётных позициях в двоичном представлении числа n.

Биты нумеруются справа налево, начиная с индекса 0.

Необходимо вернуть массив [even, odd].

Примеры:
Ввод: n = 50
Вывод: [1, 2]

Ввод: n = 2
Вывод: [0, 1]
'''

from typing import List

def even_odd_bit(n: int) -> List[int]:
    even = 0
    odd = 0
    index = 0

    while n > 0:
        if n & 1:
            if index % 2 == 0:
                even += 1
            else:
                odd += 1
        n >>= 1
        index += 1

    return [even, odd]