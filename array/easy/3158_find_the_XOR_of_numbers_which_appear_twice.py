'''
You are given an array numbers, where each number appears either once or twice.
Return the bitwise XOR of all numbers that appear twice in the array.
If no number appears twice, return 0.

Дан массив numbers, в котором каждое число встречается либо один раз, либо два раза.
Нужно вернуть результат побитового XOR всех чисел, которые встречаются дважды.
Если таких чисел нет, верни 0.
'''

from typing import List
from collections import Counter

def duplicate_numbers_XOR(numbers: List[int]) -> int:
    counts = Counter(numbers)

    result = 0
    for number, frequency in counts.items():
        if frequency == 2:
            result ^= number

    return result