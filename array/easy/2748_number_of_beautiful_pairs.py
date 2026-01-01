'''
You are given a 0-indexed integer array numbers.

A pair of indices (i, j) is called beautiful if the following conditions are satisfied:
    - 0 ≤ i < j < numbers.length;
    - the first digit of numbers[i] and the last digit of numbers[j] are coprime.

Two integers x and y are said to be coprime if they share no common divisor greater than 1.

Equivalently, x and y are coprime if: gcd(x, y) == 1, where gcd(x, y) denotes the greatest common divisor of x and y.

Return the total number of beautiful pairs in the array numbers.

Examples:
Input: numbers = [2, 5, 1, 4]
Output: 5

Input: numbers = [11, 21, 12]
Output: 2

Дан 0-индексированный массив целых чисел numbers.

Пара индексов (i, j) называется красивой, если выполняются следующие условия:
    - 0 ≤ i < j < numbers.length;
    - первая цифра числа numbers[i] и последняя цифра числа numbers[j] являются взаимно простыми.

Два целых числа x и y называются взаимно простыми, если у них нет общего делителя больше 1.

Эквивалентно, числа x и y взаимно просты, если: gcd(x, y) == 1, где gcd(x, y) - наибольший общий делитель чисел x и y.

Необходимо вернуть общее количество красивых пар в массиве numbers.

Примеры:
Ввод: numbers = [2, 5, 1, 4]
Вывод: 5

Ввод: numbers = [11, 21, 12]
Вывод: 2
'''

from typing import List
import math

def count_beautiful_pairs(numbers: List[int]) -> int:
    number_of_beautiful_pairs = 0
    length_of_numbers = len(numbers)

    for first_index in range(length_of_numbers):
        first_digit = int(str(numbers[first_index])[0])

        for second_index in range(first_index + 1, length_of_numbers):
            last_digit = numbers[second_index] % 10

            if math.gcd(first_digit, last_digit) == 1:
                number_of_beautiful_pairs += 1

    return number_of_beautiful_pairs