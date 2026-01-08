'''
You are given a 0-indexed 2D integer matrix grid of size n × n, where each element has a value in the range [1, n²].

Each integer in this range appears exactly once, except:
    - one integer a, which appears twice,
    - one integer b, which is missing from the matrix.

Your task is to identify the repeating number a and the missing number b.

Return a 0-indexed integer array ans of size 2 such that:
    - ans[0] = a;
    - ans[1] = b.

Examples:
Input: grid = [ [1, 3],
                [2, 2]
        ]
Output: [2, 4]

Input: grid = [ [9, 1, 7],
                [8, 9, 2],
                [3, 4, 6]
        ]
Output: [9, 5]

Дана двумерная целочисленная матрица grid размера n × n с нумерацией индексов с нуля, содержащая числа в диапазоне [1, n²].

Каждое число из этого диапазона встречается ровно один раз, за исключением:
    - одного числа a, которое встречается дважды,
    - одного числа b, которое отсутствует в матрице.

Необходимо найти повторяющееся число a и пропущенное число b.

Верните целочисленный массив ans длины 2, где:
    - ans[0] = a;
    - ans[1] = b.

Примеры:
Ввод: grid = [  [1, 3],
                [2, 2]
        ]
Вывод: [2, 4]

Ввод: grid = [  [9, 1, 7],
                [8, 9, 2],
                [3, 4, 6]
        ]
Вывод: [9, 5]
'''

from typing import List

def find_missing_and_repeated_values(grid: List[List[int]]) -> List[int]:
    n = len(grid)
    seen = set()
    repeated = -1

    for row in grid:
        for value in row:
            if value in seen:
                repeated = value
            else:
                seen.add(value)

    missing = -1
    for number in range(1, n * n + 1):
        if number not in seen:
            missing = number
            break

    return [repeated, missing]