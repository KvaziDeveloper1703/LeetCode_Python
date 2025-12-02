'''
You are given an array of integers numbers and an integer original, which is the first value you need to search for in numbers.

Perform the following process:
    - If original is found in numbers, multiply it by 2;
    - If it is not found, stop.

Repeat the process with the new value of original as long as it keeps appearing in numbers.

Return the final value of original.

Examples:
Input: numbers = [5, 3, 6, 1, 12], original = 3
Output: 24

Input: numbers = [2, 7, 9], original = 4
Output: 4

Дан массив целых чисел numbers и число original, которое нужно сначала искать в массиве.

Выполняется следующий процесс:
    - Если original найден в numbers, умножьте его на 2;
    - Если его нет в массиве — процесс заканчивается.

Повторяйте шаги, пока новое значение original продолжает встречаться в numbers.

Верните итоговое значение original.

Примеры:
Ввод: numbers = [5, 3, 6, 1, 12], original = 3
Вывод: 24

Ввод: numbers = [2, 7, 9], original = 4
Вывод: 4
'''

from typing import List

def find_final_value(numbers: List[int], original: int) -> int:
    numbers_set = set(numbers)

    while original in numbers_set:
        original = original * 2

    return original