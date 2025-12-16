'''
You are given an array numbers consisting of non-negative integers.

In one operation, you must do the following:
    - Choose a positive integer x such that x is less than or equal to the smallest non-zero element in numbers;
    - Subtract x from every positive element in numbers.

Your task is to return the minimum number of operations required to make all elements in numbers equal to 0.

Examples:
Input: numbers = [1, 5, 0, 3, 5]
Output: 3

Input: numbers = [0]
Output: 0

Вам дан массив numbers, состоящий из неотрицательных целых чисел.

За одну операцию необходимо выполнить следующее:
    - Выбрать положительное целое число x, такое что x меньше либо равно наименьшему ненулевому элементу массива numbers;
    - Вычесть x из каждого положительного элемента массива numbers.

Требуется определить минимальное количество операций, необходимое для того, чтобы все элементы массива стали равны 0.

Примеры:
Ввод: numbers = [1, 5, 0, 3, 5]
Вывод: 3

Ввод: numbers = [0]
Вывод: 0
'''

from typing import List

def minimum_operations(numbers: List[int]) -> int:
    positive_values = set()

    for value in numbers:
        if value > 0:
            positive_values.add(value)

    return len(positive_values)