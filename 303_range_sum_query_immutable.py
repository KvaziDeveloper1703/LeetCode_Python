'''
You are given an integer array nums. You need to handle multiple queries of the following type:
Calculate the sum of the elements of nums between indices left and right inclusive, where left <= right.

Implement the class NumArray with the following methods:
+ NumArray(int[] nums): Initializes the object with the given integer array nums.
+ int sumRange(int left, int right): Returns the sum of the elements between indices left and right inclusive (i.e., nums[left] + nums[left + 1] + ... + nums[right]).

Example:
Input: ["NumArray", "sumRange", "sumRange", "sumRange"], [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output: [null, 1, -1, -3]

Вам дан массив целых чисел nums. Необходимо обрабатывать несколько запросов следующего типа:
Вычислить сумму элементов массива nums на отрезке между индексами left и right включительно, где left <= right.

Реализуйте класс NumArray с двумя методами:
+ NumArray(int[] nums): конструктор, инициализирующий объект с переданным массивом nums.
+ int sumRange(int left, int right): возвращает сумму элементов массива с индекса left по индекс right включительно (то есть nums[left] + nums[left + 1] + ... + nums[right]).

Пример:
Ввод: ["NumArray", "sumRange", "sumRange", "sumRange"], [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Вывод: [null, 1, -1, -3]
'''

from typing import List

class NumArray:
    def __init__(self, numbers: List[int]):
        self.prefix = [0]
        for number in numbers:
            self.prefix.append(self.prefix[-1] + number)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]