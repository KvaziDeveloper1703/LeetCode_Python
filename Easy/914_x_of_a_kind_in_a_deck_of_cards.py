'''
Given an integer array deck, where deck[i] represents the number written on the i-th card.

You need to partition the deck into one or more groups such that:
    1) Each group has exactly x cards, where x > 1, and
    2) All cards in the same group have the same number written on them.

Return True if such a partition is possible, otherwise return False.

Examples:
Input: deck = [1, 2, 3, 4, 4, 3, 2, 1]
Output: True

Input: deck = [1, 1, 1, 2, 2, 2, 3, 3]
Output: False

Дан массив целых чисел deck, где deck[i] — число, написанное на i-й карточке.

Необходимо разделить карточки на одну или несколько групп так, чтобы:
    1) В каждой группе было ровно x карточек, где x > 1, и
    2) Все карточки в группе имели одинаковое число.

Верните True, если такая группировка возможна, иначе — False.

Примеры:
Ввод: deck = [1, 2, 3, 4, 4, 3, 2, 1]
Вывод: True

Ввод: deck = [1, 1, 1, 2, 2, 2, 3, 3]
Вывод: False
'''

from typing import List
from collections import Counter
from math import gcd
from functools import reduce

def has_groups_size_x(deck: List[int]) -> bool:
    counts = Counter(deck).values()
    group_size = reduce(gcd, counts)
    return group_size > 1