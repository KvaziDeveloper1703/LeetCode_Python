'''
Given an array numbers, return True if the array could have originally been sorted in non-decreasing order and then rotated some number of positions. Otherwise, return False.

Duplicates may be present in the original array.

A rotation of an array A by x positions creates an array B such that B[i] = A[(i + x) % A.length] for every valid index i.

Examples:
Input: numbers = [3,4,5,1,2]
Output: True

Input: numbers = [2,1,3,4]
Output: False

Дан массив numbers. Верните True, если массив мог быть изначально отсортирован по неубыванию, а затем ротирован на некоторое количество позиций. Иначе верните False.

В исходном массиве могут быть дубликаты.

Ротация массива A на x позиций создаёт массив B, такой что B[i] = A[(i + x) % A.length] для каждого допустимого индекса i.

Примеры:
Ввод: numbers = [3,4,5,1,2]
Вывод: True

Ввод: numbers = [2,1,3,4]
Вывод: False.
'''

from typing import List

def check(numbers: List[int]) -> bool:
    count = 0
    n = len(numbers)

    for i in range(n):
        if numbers[i] > numbers[(i + 1) % n]:
            count += 1
            if count > 1:
                return False

    return True