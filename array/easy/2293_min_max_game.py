'''
You are given a 0-indexed integer array numbers whose length is a power of 2.
Apply the following algorithm to numbers:
    - Let n be the length of numbers;
    - If n == 1, stop the process;
    - Otherwise, create a new 0-indexed integer array newNumbers of length n / 2;
    - For each index i such that 0 ≤ i < n / 2:
        - If i is even, set newNumbers[i] = min(numbers[2 * i], numbers[2 * i + 1]);
        - If i is odd, set newNumbers[i] = max(numbers[2 * i], numbers[2 * i + 1]).
    - Replace the array numbers with newNumbers;
    - Repeat the process starting from step 1.

Return the last remaining number in numbers after the algorithm finishes.

Examples:
Input: numbers = [1, 3, 5, 2, 4, 8, 2, 2]
Output: 1

Input: numbers = [3]
Output: 3

Дан целочисленный массив numbers с индексацией с нуля, длина которого является степенью двойки.
К массиву numbers применяется следующий алгоритм:
    - Пусть n - длина массива numbers;
    - Если n == 1, процесс завершается;
    - В противном случае создаётся новый целочисленный массив с индексацией с нуля newNumbers длины n / 2;
    - Для каждого индекса i, где 0 ≤ i < n / 2:
        - Если i - чётный, то newNumbers[i] = min(numbers[2 * i], numbers[2 * i + 1]);
        - Если i - нечётный, то newNumbers[i] = max(numbers[2 * i], numbers[2 * i + 1]).
    - Массив numbers заменяется на newNumbers;
    - Процесс повторяется, начиная с шага 1.

Необходимо вернуть последнее оставшееся число в массиве numbers после завершения алгоритма.

Примеры:
Ввод: numbers = [1, 3, 5, 2, 4, 8, 2, 2]
Вывод: 1

Ввод: numbers = [3]
Вывод: 3
'''

from typing import List

def min_max_game(numbers: List[int]) -> int:
    while len(numbers) > 1:
        new_numbers = []
        for index in range(len(numbers) // 2):
            if index % 2 == 0:
                new_numbers.append(min(numbers[2 * index], numbers[2 * index + 1]))
            else:
                new_numbers.append(max(numbers[2 * index], numbers[2 * index + 1]))
        numbers = new_numbers
    return numbers[0]