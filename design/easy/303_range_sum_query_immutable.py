'''
You are given an integer array numbers. You need to handle multiple queries of the following type:
Calculate the sum of the elements of numbers between indices left and right inclusive, where left <= right.

Implement the class NumArray with the following methods:
    + NumArray(int[] numbers): Initializes the object with the given integer array numbers.
    + int sum_range(int left, int right): Returns the sum of the elements between indices left and right inclusive (i.e., numbers[left] + numbers[left + 1] + ... + numbers[right]).

Example:
Input: ["NumArray", "sum_range", "sum_range", "sum_range"], [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output: [null, 1, -1, -3]

Вам дан массив целых чисел numbers. Необходимо обрабатывать несколько запросов следующего типа:
Вычислить сумму элементов массива numbers на отрезке между индексами left и right включительно, где left <= right.

Реализуйте класс NumArray с двумя методами:
    + NumArray(int[] numbers): конструктор, инициализирующий объект с переданным массивом numbers.
    + int sum_range(int left, int right): возвращает сумму элементов массива с индекса left по индекс right включительно (то есть numbers[left] + numbers[left + 1] + ... + numbers[right]).

Пример:
Ввод: ["NumArray", "sum_range", "sum_range", "sum_range"], [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Вывод: [null, 1, -1, -3]
'''

from typing import List

class NumArray:
    def __init__(self, numbers: List[int]):
        self.prefix = [0]
        for number in numbers:
            self.prefix.append(self.prefix[-1] + number)

    def sum_range(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]