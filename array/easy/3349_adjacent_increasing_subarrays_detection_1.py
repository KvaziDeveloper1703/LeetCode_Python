'''
You are given an integer array numbers of length n and an integer k.

Determine whether it is possible to find two adjacent subarrays, each of length k, such that both subarrays are strictly increasing.

More precisely, check if there exist indices a and b (a < b) such that:
    - The subarray numbers[a .. a + k - 1] is strictly increasing;
    - The subarray numbers[b .. b + k - 1] is strictly increasing;
    - The two subarrays are adjacent, meaning b = a + k.

Return true if such subarrays exist; otherwise, return false.

Input: numbers = [2,5,7,8,9,2,3,4,3,1], k = 3
Output: true

Input: numbers = [1,2,3,4,4,4,4,5,6,7], k = 5
Output: false

Дан массив целых чисел numbers длины n и целое число k.

Необходимо определить, существуют ли два соседних подмассива длины k, такие что оба подмассива строго возрастающие.

Более формально, требуется проверить, существуют ли индексы a и b (a < b), для которых выполняются условия:
    - Подмассив numbers[a .. a + k - 1] является строго возрастающим;
    - Подмассив numbers[b .. b + k - 1] является строго возрастающим;
    - Подмассивы являются соседними, то есть b = a + k.

Верните true, если такие подмассивы существуют, и false - в противном случае.

Ввод: numbers = [2,5,7,8,9,2,3,4,3,1], k = 3
Вывод: true

Ввод: numbers = [1,2,3,4,4,4,4,5,6,7], k = 5
Вывод: false
'''

from typing import List

def has_increasing_subarrays(numbers: List[int], k: int) -> bool:
    n = len(numbers)
    if 2 * k > n:
        return False

    increasing_length = [1] * n

    for i in range(1, n):
        if numbers[i] > numbers[i - 1]:
            increasing_length[i] = increasing_length[i - 1] + 1
        else:
            increasing_length[i] = 1

    for start in range(n - 2 * k + 1):
        first_end = start + k - 1
        second_end = start + 2 * k - 1

        if increasing_length[first_end] >= k and increasing_length[second_end] >= k:
            return True

    return False