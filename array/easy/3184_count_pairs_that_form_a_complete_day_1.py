'''
You are given an integer array hours, where each element represents a time duration in hours.

Return the number of pairs of indices (i, j) such that:
    - i < j;
    - hours[i] + hours[j] forms a complete day.

A complete day means that the total number of hours is divisible by 24, i.e. it is an exact multiple of 24.

Examples:
Input: hours = [12, 12, 30, 24, 24]
Output: 2

Input: hours = [72, 48, 24, 3]
Output: 3

Дан целочисленный массив hours, где каждый элемент обозначает длительность времени в часах.

Нужно вернуть количество пар индексов (i, j) таких, что:
    - i < j;
    - hours[i] + hours[j] образует полный день.

Полный день означает, что сумма часов делится на 24 без остатка, то есть является точным кратным 24.

Примеры:
Ввод: hours = [12, 12, 30, 24, 24]
Вывод: 2

Ввод: hours = [72, 48, 24, 3]
Вывод: 3
'''

from typing import List

def count_complete_day_pairs(hours: List[int]) -> int:
    remainder_counts = [0] * 24
    pairs_count = 0

    for hour_value in hours:
        remainder = hour_value % 24
        needed_remainder = (24 - remainder) % 24

        pairs_count += remainder_counts[needed_remainder]
        remainder_counts[remainder] += 1

    return pairs_count