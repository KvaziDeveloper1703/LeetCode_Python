'''
You are given a 0-indexed integer array numbers of length n, and an integer k.

Your task is to return the number of pairs (i, j) such that:
    - 0≤i<j<n,
    - numbers[i]=numbers[j],
    - (i⋅j) is divisible by k.

Examples:
Input: numbers = [3,1,2,2,2,1,3], k = 2
Output: 4

Input: numbers = [1,2,3,4], k = 1
Output: 0

Дан целочисленный массив numbers, индексируемый с 0, длиной n, и целое число k.

Требуется найти количество пар (i, j), для которых выполняются условия:
    - 0≤i<j<n,
    - numbers[i]=numbers[j],
    - произведение индексов i⋅j делится на k.

Примеры:
Ввод: numbers = [3,1,2,2,2,1,3], k = 2
Вывод: 4

Ввод: numbers = [1,2,3,4], k = 1
Вывод: 0
'''

from typing import List

def count_pairs(numbers: List[int], k: int) -> int:
    count = 0
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] == numbers[j] and (i * j) % k == 0:
                count += 1
    return count