'''
A super ugly number is a positive integer whose prime factors are all contained in the array primes.

Given an integer n and an array of integers primes, return the nth super ugly number.

Example:
Input: primes = [2, 7, 13, 19]
Output: 32

Input: primes = [2, 3, 5]
Output: 1

Сверх уродливое число — это положительное целое число, все простые делители которого содержатся в массиве primes.

Дано целое число n и массив целых чисел primes. Необходимо вернуть n-е сверх уродливое число.

Примеры:
Ввод: primes = [2, 7, 13, 19]
Вывод: 32
'''

from heapq import heappush, heappop
from typing import List

def nth_super_ugly_number(n: int, primes: List[int]) -> int:
    ugly = [1]
    heap = []

    for prime in primes:
        heappush(heap, (prime, prime, 0))

    while len(ugly) < n:
        next_ugly, prime, index = heappop(heap)

        if next_ugly != ugly[-1]:
            ugly.append(next_ugly)

        heappush(heap, (prime * ugly[index + 1], prime, index + 1))

    return ugly[-1]