'''
Given an integer array my_array and three integers a, b, and c.
You need to find the number of good triplets.

A triplet (my_array[i], my_array[j], my_array[k]) is good if the following conditions hold:
    + 0 <= i < j < k < my_array.length
    + |my_array[i] - my_array[j]| <= a
    + |my_array[j] - my_array[k]| <= b
    + |my_array[i] - my_array[k]| <= c

Return the number of such triplets.

Examples:
Input: my_array = [3,0,1,1,9,7], a = 7, b = 2, c = 3
Output: 4

Input: my_array = [1,1,2,2,3], a = 0, b = 0, c = 1
Output: 0

Дан массив целых чисел my_array и три целых числа a, b и c.
Нужно найти количество хороших троек.

Тройка элементов (my_array[i], my_array[j], my_array[k]) называется хорошей, если выполняются условия:
    + 0 <= i < j < k < my_array.length
    + |my_array[i] - my_array[j]| <= a
    + |my_array[j] - my_array[k]| <= b
    + |my_array[i] - my_array[k]| <= c

Нужно вернуть количество таких троек.

Примеры:
Ввод: my_array = [3,0,1,1,9,7], a = 7, b = 2, c = 3
Вывод: 4

Ввод: my_array = [1,1,2,2,3], a = 0, b = 0, c = 1
Вывод: 0
'''

from typing import List

def count_good_triplets(my_array: List[int], a: int, b: int, c: int) -> int:
    n = len(my_array)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if abs(my_array[i] - my_array[j]) <= a:
                for k in range(j + 1, n):
                    if abs(my_array[j] - my_array[k]) <= b and abs(my_array[i] - my_array[k]) <= c:
                        count += 1
    return count