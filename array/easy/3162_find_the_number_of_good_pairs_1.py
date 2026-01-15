'''
You are given two integer arrays numbers1 and numbers2 of lengths n and m, and a positive integer k.

A pair of indices (i, j) is called good if: numbers1[i] is divisible by numbers2[j] · k.
That is: numbers1[i] % (numbers2[j] * k) == 0.

Return the total number of good pairs.

Даны два целочисленных массива numbers1 и numbers2 длиной n и m, а также положительное целое число k.

Пара индексов (i, j) называется хорошей, если выполняется условие: numbers1[i] делится на numbers2[j] · k без остатка.
То есть: numbers1[i] % (numbers2[j] * k) == 0.

Нужно вернуть общее количество хороших пар.
'''

from typing import List
from collections import Counter

def number_of_pairs(numbers_1: List[int], numbers_2: List[int], k: int) -> int:
    numbers_2_counts = Counter(numbers_2)
    good_pairs_count = 0

    for number_in_numbers_1 in numbers_1:
        if number_in_numbers_1 % k != 0:
            continue

        reduced_value = number_in_numbers_1 // k

        divisor = 1
        while divisor * divisor <= reduced_value:
            if reduced_value % divisor == 0:
                other_divisor = reduced_value // divisor

                good_pairs_count += numbers_2_counts.get(divisor, 0)

                if other_divisor != divisor:
                    good_pairs_count += numbers_2_counts.get(other_divisor, 0)

            divisor += 1

    return good_pairs_count