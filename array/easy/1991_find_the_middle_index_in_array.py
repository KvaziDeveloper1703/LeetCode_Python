'''
You are given a 0-indexed integer array numbers. Find the leftmost middleIndex.

A middleIndex is an index such that: numbers[0] + numbers[1] + ... + numbers[middleIndex − 1] == numbers[middleIndex + 1] + numbers[middleIndex + 2] + ... + numbers[numbers.length − 1]

If middleIndex == 0, the left sum is considered 0.
If middleIndex == numbers.length − 1, the right sum is considered 0.

Return the leftmost middleIndex that satisfies the condition, or -1 if no such index exists.

Examples:
Input: numbers = [2,3,-1,8,4]
Output: 3

Input: numbers = [1,-1,4]
Output: 2

Дан целочисленный массив numbers, индексируемый с нуля.
Нужно найти самый левый индекс middleIndex, то есть минимальный индекс, удовлетворяющий условию.

Индекс middleIndex - это такой индекс, что: numbers[0] + numbers[1] + ... + numbers[middleIndex − 1] == numbers[middleIndex + 1] + numbers[middleIndex + 2] + ... + numbers[numbers.length − 1]

Если middleIndex == 0, сумма слева считается 0.
Если middleIndex == numbers.length − 1, сумма справа считается 0.

Верните самый левый подходящий middleIndex, или -1, если такого индекса нет.

Примеры:
Ввод: numbers = [2,3,-1,8,4]
Вывод: 3

Ввод: numbers = [1,-1,4]
Вывод: 2
'''

from typing import List

def find_middle_index(numbers: List[int]) -> int:
    total_sum = sum(numbers)
    left_sum = 0

    for index, value in enumerate(numbers):
        right_sum = total_sum - left_sum - value
        if left_sum == right_sum:
            return index
        left_sum += value

    return -1