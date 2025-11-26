'''
You are given three integer arrays: numbers_1, numbers_2, and numbers_3.
Your task is to return an array of distinct values that appear in at least two of the three arrays.

You may return the result in any order.

Даны три целочисленных массива: numbers_1, numbers_2 и numbers_3.
Требуется вернуть массив уникальных значений, которые встречаются как минимум в двух из этих трёх массивов.

Порядок элементов в ответе может быть любым.
'''

from typing import List

def two_out_of_three(numbers_1: List[int], numbers_2: List[int], numbers_3: List[int]) -> List[int]:
        set_1 = set(numbers_1)
        set_2 = set(numbers_2)
        set_3 = set(numbers_3)

        result = set()

        for value in set_1:
            if value in set_2 or value in set_3:
                result.add(value)

        for value in set_2:
            if value in set_1 or value in set_3:
                result.add(value)

        return list(result)