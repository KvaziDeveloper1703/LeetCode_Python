'''
Given an integer array numbers. Design a class Solution to:
    + Solution(int[] numbers): Initialize the object with the integer array numbers;
    + int[] reset(): Reset the array to its original configuration and return it;
    + int[] shuffle(): Return a random shuffling of the array. All permutations must be equally likely.

Example:
Input: ["Solution", "shuffle", "reset", "shuffle"], [[[1, 2, 3]], [], [], []]
Output: [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

Вам дан массив целых чисел numbers. Необходимо реализовать класс Solution, который поддерживает следующие методы:
    + Solution(int[] numbers): Конструктор, инициализирующий объект с массивом numbers;
    + int[] reset(): Сбрасывает массив в исходную конфигурацию и возвращает его;
    + int[] shuffle(): Возвращает случайную перестановку элементов массива. Все возможные перестановки должны быть равновероятными.

Пример:
Ввод: ["Solution", "shuffle", "reset", "shuffle"], [[[1, 2, 3]], [], [], []]
Вывод: [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]
'''

import random
from typing import List

class Solution:
    def __init__(self, numbers: List[int]):
        self.original = numbers[:]
        self.array = numbers[:]

    def reset(self) -> List[int]:
        self.array = self.original[:]
        return self.array

    def shuffle(self) -> List[int]:
        shuffled = self.array[:]
        n = len(shuffled)
        for i in range(n):
            j = random.randint(i, n - 1)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
        return shuffled