'''
You are given a 0-indexed two-dimensional integer array numbers.

Return the largest prime number that appears on at least one of the diagonals of numbers. If there is no prime number on any diagonal, return 0.

Input: numbers = [[1,2,3],[5,6,7],[9,10,11]]
Output: 11

Input: numbers = [[1,2,3],[5,17,7],[9,11,10]]
Output: 17

Дан двумерный целочисленный массив numbers с индексацией, начинающейся с 0.

Необходимо вернуть наибольшее простое число, которое находится хотя бы на одной из диагоналей массива numbers. Если на диагоналях нет ни одного простого числа, верните 0.

Ввод: numbers = [[1,2,3],[5,6,7],[9,10,11]]
Вывод: 11

Ввод: numbers = [[1,2,3],[5,17,7],[9,11,10]]
Вывод: 17
'''

from typing import List
import math

def diagonal_prime(numbers: List[List[int]]) -> int:
    size = len(numbers)
    largest_prime = 0

    def is_prime(number: int) -> bool:
        if number <= 1:
            return False
        if number <= 3:
            return True
        if number % 2 == 0:
            return number == 2
        limit = int(math.sqrt(number)) + 1
        for divisor in range(3, limit, 2):
            if number % divisor == 0:
                return False
        return True

    for index in range(size):
        primary_diagonal_value = numbers[index][index]
        secondary_diagonal_value = numbers[index][size - index - 1]

        if is_prime(primary_diagonal_value):
            largest_prime = max(largest_prime, primary_diagonal_value)

        if is_prime(secondary_diagonal_value):
            largest_prime = max(largest_prime, secondary_diagonal_value)

    return largest_prime