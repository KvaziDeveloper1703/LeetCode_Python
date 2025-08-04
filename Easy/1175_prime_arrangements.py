'''
Given an integer n.

Return the number of permutations of numbers from 1 to n such that all prime numbers appear only at prime indices.

Examples:
Input: n = 5
Output: 12

Input: n = 100
Output: 682289015

Дано целое число n.

Нужно найти количество перестановок чисел от 1 до n таких, что все простые числа находятся только на простых позициях.

Примеры:
Ввод: n = 5
Вывод: 12

Ввод: n = 100
Вывод: 682289015
'''

from typing import List

MOD = 10**9 + 7

def count_primes(n: int) -> int:
    if n < 2:
        return 0
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    i = 2
    while i * i <= n:
        if sieve[i]:
            step = i
            start = i * i
            sieve[start:n+1:step] = [False] * ((n - start) // step + 1)
        i += 1
    return sum(sieve)

def fact_mod(x: int) -> int:
    result = 1
    for v in range(2, x + 1):
        result = (result * v) % MOD
    return result

def number_of_prime_arrangements(n: int) -> int:
    p = self.count_primes(n)
    return (self.fact_mod(p) * self.fact_mod(n - p)) % MOD