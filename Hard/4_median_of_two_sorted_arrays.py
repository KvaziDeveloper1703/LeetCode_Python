'''
You are given two sorted arrays, numbers_1 and numbers_2, of sizes m and n respectively. 
Your task is to find the median of the merged sorted array formed by combining these two arrays.
The overall time complexity should be O(log(m + n)).

Example:
Input: numbers_1 = [1, 3], numbers_2 = [2]
Output: 2.00000

Даны два отсортированных массива numbers_1 и numbers_2 размеров m и n соответственно. 
Нужно найти медиану объединённого отсортированного массива, составленного из этих двух.
Алгоритм должен работать за время O(log(m + n)).

Пример:
Ввод: numbers_1 = [1, 3], numbers_2 = [2]
Вывод: 2.00000
'''

from typing import List

def find_median_sorted_arrays(numbers_1: List[int], numbers_2: List[int]) -> float:
    if len(numbers_1) > len(numbers_2):
        numbers_1, numbers_2 = numbers_2, numbers_1

        m, n = len(numbers_1), len(numbers_2)
        half_len = (m + n + 1) // 2

        low, high = 0, m
        while low <= high:
            i = (low + high) // 2
            j = half_len - i

            if i < m and numbers_2[j - 1] > numbers_1[i]:
                low = i + 1
            elif i > 0 and numbers_1[i - 1] > numbers_2[j]:
                high = i - 1
            else:
                if i == 0:
                    max_of_left = numbers_2[j - 1]
                elif j == 0:
                    max_of_left = numbers_1[i - 1]
                else:
                    max_of_left = max(numbers_1[i - 1], numbers_2[j - 1])

                if (m + n) % 2 == 1:
                    return float(max_of_left)

                if i == m:
                    min_of_right = numbers_2[j]
                elif j == n:
                    min_of_right = numbers_1[i]
                else:
                    min_of_right = min(numbers_1[i], numbers_2[j])

                return (max_of_left + min_of_right) / 2.0