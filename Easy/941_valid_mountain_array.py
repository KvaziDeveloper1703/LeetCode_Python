'''
Given an array of integers my_array. Return True if and only if it is a valid mountain array.

A mountain array must satisfy all the following:
    + my_array.length >= 3
    + There exists an index i (with 0 < i < my_array.length - 1) such that:
        + my_array[0] < my_array[1] < ... < my_array[i - 1] < my_array[i]
        + my_array[i] > my_array[i + 1] > ... > my_array[my_array.length - 1]

In other words, the array strictly increases to a single peak, and then strictly decreases afterward. The peak cannot be the first or last element.

Examples:
Input: my_array = [2,1]
Output: False

Input: my_array = [3,5,5]
Output: False

Дан массив целых чисел my_array. Верните True только в том случае, если массив является горным массивом.

Массив считается горным, если выполняются все условия:
    + my_array.length >= 3
    + Существует индекс i (где 0 < i < my_array.length - 1), такой что:
        + my_array[0] < my_array[1] < ... < my_array[i - 1] < my_array[i] — сначала массив строго возрастает
        + my_array[i] > my_array[i + 1] > ... > my_array[my_array.length - 1] — затем строго убывает

Иными словами, массив должен сначала строго возрастать до одной вершины, а затем строго убывать. Вершина не может быть первым или последним элементом.

Примеры:
Ввод: my_array = [2,1]
Вывод: False

Ввод: my_array = [3,5,5]
Вывод: False
'''

from typing import List

def valid_mountain_array(my_array: List[int]) -> bool:
    n = len(my_array)
    if n < 3:
        return False

    i = 0

    while i + 1 < n and my_array[i] < my_array[i + 1]:
        i += 1

    if i == 0 or i == n - 1:
        return False

    while i + 1 < n and my_array[i] > my_array[i + 1]:
        i += 1

    return i == n - 1