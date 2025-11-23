'''
The product difference between two pairs (a,b) and (c,d) is defined as: (a×b)−(c×d)

For example, the product difference between (5,6) and (2,7) is (5×6)−(2×7)=16.

Given an integer array numbers, choose four distinct indices w,x,y,z such that the product difference between the pairs (numbers[w],numbers[x]) and (numbers[y],numbers[z]) is maximized.

Return the maximum possible product difference.

Examples:
Input: numbers = [5, 6, 2, 7, 4]
Output: 34

Input: numbers = [4, 2, 5, 9, 7, 4, 8]
Output: 64

Разность произведений между двумя парами (a,b) и (c,d) определяется как: (a×b)−(c×d)

Например, разность произведений между парами (5,6) и (2,7) равна (5×6)−(2×7)=16.

Дан целочисленный массив numbers. Выберите четыре различных индекса w,x,y,z так, чтобы разность произведений пар (numbers[w],numbers[x]) и (numbers[y],numbers[z]) была максимальной.

Верните максимально возможную разность произведений.
'''

from typing import List

def max_product_difference(numbers: List[int]) -> int:
    max_first = -10**9
    max_second = -10**9
    min_first = 10**9
    min_second = 10**9

    for value in numbers:
        if value > max_first:
            max_second = max_first
            max_first = value
        elif value > max_second:
            max_second = value

        if value < min_first:
            min_second = min_first
            min_first = value
        elif value < min_second:
            min_second = value

    product_max = max_first * max_second
    product_min = min_first * min_second

    return product_max - product_min