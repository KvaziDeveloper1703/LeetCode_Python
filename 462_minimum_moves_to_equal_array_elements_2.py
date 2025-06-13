"""
Given an integer array numbers of size N, return the minimum number of moves required to make all array elements equal.
In one move, you can increment or decrement any single element of the array by 1.
It is guaranteed that the result will fit in a 32-bit integer.

Examples:
Input: numbers = [1, 2, 3]
Output: 2

Input: numbers = [1, 10, 2, 9]
Output: 16

Дан целочисленный массив numbers длины N. Верните минимальное количество шагов, необходимых для того, чтобы все элементы массива стали равными.
За один шаг можно увеличить или уменьшить значение одного элемента массива на 1.
Гарантируется, что ответ помещается в 32-битное целое число.

Примеры:
Ввод: numbers = [1, 2, 3]
Вывод: 2

Пример 2:
Ввод: numbers = [1, 10, 2, 9]
Вывод: 16
"""

def minMoves2(numbers: list[int]) -> int:
    numbers.sort()

    N = len(numbers)
    median = numbers[N // 2]

    total_moves = 0
    for number in numbers:
        distance = abs(number - median)
        total_moves += distance

    return total_moves