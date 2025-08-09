'''
Given an integer array my_array, determine if there exist two indices i and j such that: 
    + i!=j;
    + 0<=i, j<my_array.length;
    + my_array[i]=2×my_array[j].

Examples:
Input: my_array = [10, 2, 5, 3]
Output: True

Input: my_array = [3, 1, 7, 11]
Output: False

Дан массив целых чисел my_array. Определите, существуют ли два индекса i и j, такие что:
    + i!=j;
    + 0<=i, j<my_array.length;
    + my_array[i]=2×my_array[j].

Примеры:
Ввод: my_array = [10, 2, 5, 3]
Вывод: True

Ввод: my_array = [3, 1, 7, 11]
Вывод: False
'''

from typing import List

def check_if_exist(my_array: List[int]) -> bool:
    seen = set()
    for x in my_array:
        if 2 * x in seen or (x % 2 == 0 and x // 2 in seen):
            return True
        seen.add(x)
    return False