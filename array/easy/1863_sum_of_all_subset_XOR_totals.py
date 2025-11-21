'''
The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

For example, the XOR total of [2, 5, 6] is 2 XOR 5 XOR 6 = 1.

Given an array numbers, return the sum of the XOR totals of all subsets of numbers.

An array a is considered a subset of an array b if a can be formed by removing some elements from b.

XOR-сумма массива определяется как побитовое XOR всех его элементов, или 0, если массив пустой.

Например, XOR-сумма массива [2, 5, 6] равна 2 XOR 5 XOR 6 = 1.

Дан массив numbers. Нужно вернуть сумму XOR-сумм всех подмножеств массива numbers.

Массив a является подмножеством массива b, если его можно получить, удалив из b некоторые элементы.
'''

from typing import List

def subset_XOR_sum(numbers: List[int]) -> int:
    or_all = 0
    for number in numbers:
        or_all |= number

    return or_all * (1 << (len(numbers) - 1))