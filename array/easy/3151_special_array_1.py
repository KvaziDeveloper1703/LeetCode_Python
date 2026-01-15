'''
An array is called special if the parity of every pair of adjacent elements is different.

That means that for every neighboring pair:
    - one element must be even;
    - the other must be odd.

You are given an integer array numbers.

Return True if numbers is a special array, otherwise return False.

Массив называется специальным, если чётность каждой пары соседних элементов в нём различается.

То есть для любых двух соседних элементов:
    - один должен быть чётным;
    - второй должен быть нечётным.

Дан массив целых чисел numbers.

Верни True, если массив numbers является специальным, иначе верни False.
'''

from typing import List

def is_array_special(numbers: List[int]) -> bool:
    for index in range(1, len(numbers)):
        if numbers[index] % 2 == numbers[index - 1] % 2:
            return False
    return True