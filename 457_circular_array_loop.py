'''
You are playing a game on a circular array of non-zero integers called nums.
Each element numbers[i] tells you how many steps to move:
    + If numbers[i] > 0, move forward numbers[i] steps.
    + If numbers[i] < 0, move backward abs(numbers[i]) steps.

Since the array is circular:
    + Moving forward from the last index wraps around to the beginning.
    + Moving backward from the first index wraps around to the end.

A cycle in the array is a sequence of indices seq of length k that satisfies the following:
    1) Following the jump rules leads from seq[0] -> seq[1] -> ... -> seq[k−1] -> seq[0] -> ... infinitely.
    2) All numbers in the cycle must have the same sign — all positive or all negative.
    3) The length of the cycle k must be greater than 1.

Return true if there is at least one valid cycle, otherwise return false.

Examples:
Input: numbers = [2, -1, 1, 2, 2]
Output: true

Input: numbers = [-1, -2, -3, -4, -5, 6]
Output: false

Вы играете в игру с круговым массивом numbers, состоящим из ненулевых целых чисел.
Каждый элемент numbers[i] показывает, на сколько позиций вы должны переместиться:
    + Если numbers[i] > 0, двигайтесь вперёд на numbers[i] шагов.
    + Если numbers[i] < 0, двигайтесь назад на abs(numbers[i]) шагов.

Так как массив круговой:
    + Если выйти за последний элемент — переход происходит на первый.
    + Если выйти за первый элемент назад — переход на последний.

Цикл — это последовательность индексов seq длины k, которая удовлетворяет условиям:
    1) Переходы по правилам дают последовательность seq[0] → seq[1] → ... → seq[k−1] → seq[0] → ... бесконечно.
    2) Все элементы nums[seq[j]] должны быть одного знака — все положительные или все отрицательные.
    3) Длина цикла k > 1.

Верните true, если существует хотя бы один такой цикл, иначе верните false.

Примеры:
Ввод: numbers = [2, -1, 1, 2, 2]
Вывод: true

Ввод: numbers = [-1, -2, -3, -4, -5, 6]
Вывод: false
'''

from typing import List

def circular_array_loop(numbers: List[int]) -> bool:
    n = len(numbers)

    def next_index(i):
        return (i + numbers[i]) % n

    for i in range(n):
        if numbers[i] == 0:
            continue

        slow, fast = i, i
        direction = numbers[i] > 0

        while True:
            next_slow = next_index(slow)
            next_fast = next_index(fast)

            if numbers[next_fast] * numbers[fast] <= 0:
                break

            next_fast = next_index(next_fast)
            if numbers[next_fast] * numbers[fast] <= 0:
                break

            if numbers[next_slow] * numbers[slow] <= 0:
                break

            slow = next_slow
            fast = next_fast
            if slow == fast:
                if slow == next_index(slow):
                    break
                return True

        j = i

        while numbers[j] * numbers[i] > 0:
            next_j = next_index(j)
            numbers[j] = 0
            j = next_j

    return False