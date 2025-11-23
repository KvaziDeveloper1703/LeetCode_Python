'''
You are given an integer array numbers of length n.
You need to create a new array answer of length 2n, where:
    - answer[i] = numbers[i];
    - answer[i + n] = numbers[i].
for every index i from 0 to n - 1.

In other words, answer is the result of concatenating numbers with itself.
Return the array answer.

Examples:
Input: numbers = [1, 2, 1]
Output: [1, 2, 1, 1, 2, 1]

Input: numbers = [1, 3, 2, 1]
Output: [1, 3, 2, 1, 1, 3, 2, 1]

Дан целочисленный массив numbers длины n.
Нужно создать массив answer длины 2n, такой что:
    - answer[i] = numbers[i];
    - answer[i + n] = numbers[i].
для всех индексов от 0 до n - 1.

То есть answer - это массив numbers, записанный два раза подряд.
Верните массив answer.

Примеры:
Ввод: numbers = [1, 2, 1]
Вывод: [1, 2, 1, 1, 2, 1]

Ввод: numbers = [1, 3, 2, 1]
Вывод: [1, 3, 2, 1, 1, 3, 2, 1]
'''

from typing import List

def get_concatenation(numbers: List[int]) -> List[int]:
        return numbers + numbers