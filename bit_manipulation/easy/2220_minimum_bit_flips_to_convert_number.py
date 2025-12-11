'''
A bit flip of a number x means selecting any bit in the binary representation of x and switching it:
    - from 0 to 1, or
    - from 1 to 0.

For example, if x = 7, its binary form is 111. You may flip any bit, including leading zeros that are not shown.
    - Flipping the rightmost bit: 111 → 110;
    - Flipping the second bit: 111 → 101.

Flipping the fifth bit: 0 0 111 → 1 0 111

Given two integers start and goal, return the minimum number of bit flips needed to convert start into goal.

Examples:
Input: start = 10, goal = 7
Output: 3

Input: start = 3, goal = 4
Output: 3

Переворот бита числа x означает выбор любого бита в его двоичном представлении и изменение его значения:
    - из 0 в 1,
    - или из 1 в 0.

Например, если x = 7, его двоичное представление — 111. Можно менять любой бит, включая не показанные ведущие нули.
    - Переворот правого бита: 111 → 110;
    - Переворот второго бита справа: 111 → 101.

Переворот пятого бита: 00 111 → 10 111

Даны два целых числа start и goal. Нужно вернуть минимальное количество переворотов битов, необходимое, чтобы преобразовать число start в число goal.

Примеры:
Ввод: start = 10, goal = 7
Вывод: 3

Ввод: start = 3, goal = 4
Вывод: 3
'''

def min_bit_flips(start: int, goal: int) -> int:
    xor_value = start ^ goal
    flips = 0

    while xor_value > 0:
        if xor_value & 1:
            flips += 1
        xor_value >>= 1

    return flips