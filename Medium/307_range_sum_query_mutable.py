'''
You are given an integer array numbers. You need to handle two types of queries:
    + Update: change the value of an element in the array.
    + Range Sum: calculate the sum of the elements between indices left and right (inclusive), where left <= right.

Implement the class NumArray with the following methods:
    + NumArray(int[] numbers): Initializes the object with the given integer array numbers.
    + void update(int index, int val): Updates the value of numbers[index] to be val.
    + int sumRange(int left, int right): Returns the sum of elements between indices left and right inclusive (i.e., numbers[left] + numbers[left+1] + ... + numbers[right]).

Example:
Input: ["NumArray", "sumRange", "update", "sumRange"], [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output: [null, 9, null, 8]

Дан массив целых чисел numbers. Необходимо обрабатывать два типа запросов:
    + Обновление: изменить значение одного из элементов массива.
    + Сумма диапазона: вычислить сумму элементов массива между индексами left и right включительно, где left <= right.

Реализуйте класс NumArray со следующими методами:
    + NumArray(int[] numbers): конструктор, инициализирующий объект массивом numbers.
    + void update(int index, int val): обновляет значение numbers[index] на val.
    + int sumRange(int left, int right): возвращает сумму элементов от numbers[left] до numbers[right] включительно (то есть numbers[left] + numbers[left+1] + ... + numbers[right]).

Пример:
Ввод: ["NumArray", "sumRange", "update", "sumRange"], [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Вывод:  [null, 9, null, 8]
'''

from typing import List

class NumArray:
    def __init__(self, numbers: List[int]):
        self.n = len(numbers)
        self.tree = [0] * (2 * self.n)

        for i in range(self.n):
            self.tree[self.n + i] = numbers[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index: int, value: int) -> None:
        position = index + self.n
        self.tree[position] = value

        while position > 1:
            position //= 2
            self.tree[position] = self.tree[2 * position] + self.tree[2 * position + 1]

    def sumRange(self, left: int, right: int) -> int:
        left += self.n
        right += self.n
        total = 0

        while left <= right:
            if left % 2 == 1:
                total += self.tree[left]
                left += 1
            if right % 2 == 0:
                total += self.tree[right]
                right -= 1
            left //= 2
            right //= 2

        return total