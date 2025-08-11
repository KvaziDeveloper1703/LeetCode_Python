'''
Given an array of integers my_array, replace each element with its rank.

The rank represents how large the element is, based on the following rules:
    + Rank is a positive integer starting from 1;
    + The larger the element, the larger its rank;
    + If two elements are equal, they should have the same rank;
    + Ranks should be as small as possible.

Examples:
Input: my_array = [40, 10, 20, 30]
Output: [4, 1, 2, 3]

Input: my_array = [100, 100, 100]
Output: [1, 1, 1]

Дан массив целых чисел my_array. Замените каждый элемент на его ранг.

Ранг элемента определяется его "величиной" среди всех элементов массива по следующим правилам:
    + Ранги — это целые числа, начиная с 1;
    + Чем больше значение элемента, тем выше его ранг;
    + Если два элемента равны, они получают одинаковый ранг;
    + Ранги должны быть наименьшими возможными.

Примеры:
Ввод: my_array = [40, 10, 20, 30]
Вывод: [4, 1, 2, 3]

Ввод: my_array = [100, 100, 100]
Вывод: [1, 1, 1]
'''

from typing import List

def array_rank_transform(my_array: List[int]) -> List[int]:
    sorted_unique = sorted(set(my_array))
    rank = {number: i + 1 for i, number in enumerate(sorted_unique)}
    return [rank[number] for number in my_array]