'''
Given an array of positive integers array, determine whether there exists a pattern of length m that repeats consecutively at least k times.
A pattern is a subarray that appears multiple times in a row without overlapping. The pattern is specified by its length m and the number of repetitions.

Input:
    + array: array of positive integers;
    + m: positive integer, the length of the pattern;
    + k: positive integer, the minimum number of consecutive repetitions.

Return True if there exists a subarray of length m that repeats consecutively at least k times; otherwise return False.

Examples:
Input: array = [1,2,4,4,4,4], m = 1, k = 3
Output: True

Input: array = [1,2,1,2,1,1,1,3], m = 2, k = 2
Output: True

Дан массив положительных целых чисел array. Нужно определить, существует ли шаблон длины m, который повторяется подряд не менее k раз.
Шаблон — это подмассив, который встречается несколько раз подряд без перекрытий. Шаблон задаётся своей длиной m и числом повторений.

Входные данные:
    + array: массив положительных целых чисел;
    + m: положительное целое число — длина шаблона;
    + k: положительное целое число — минимальное число последовательных повторений.

Вернуть True, если существует подмассив длины m, который повторяется подряд как минимум k раз; иначе вернуть False.

Примеры:
Ввод: array = [1,2,4,4,4,4], m = 1, k = 3
Вывод: True

Ввод: array = [1,2,1,2,1,1,1,3], m = 2, k = 2
Вывод: True
'''

from typing import List

def contains_pattern(array: List[int], m: int, k: int) -> bool:
    n = len(array)
    for start in range(0, n - m * k + 1):
        ok = True
        for i in range(m * (k - 1)):
            if array[start + i] != array[start + i + m]:
                ok = False
                break
        if ok:
            return True
    return False