'''
You are given an integer array numbers. Your task is to find all unique triplets [numbers[i], numbers[j], numbers[k]] such that:
+ i != j, i != k, and j != k;
+ numbers[i] + numbers[j] + numbers[k] == 0.

Return a list of all such distinct triplets.

Examples:
Input: numbers = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2], [-1,0,1]]

Input: numbers = [0,1,1]
Output: []

Input: numbers = [0,0,0]
Output: [[0,0,0]]

Дан целочисленный массив numbers. Ваша задача — найти все уникальные тройки чисел [numbers[i], numbers[j], numbers[k]], такие что:
+ i != j, i != k, и j != k;
+ numbers[i] + numbers[j] + numbers[k] == 0.

Верните список всех таких различных троек.

Примеры:
Вход: numbers = [-1, 0, 1, 2, -1, -4]
Выход: [[-1, -1, 2], [-1, 0, 1]]

Вход: numbers = [0, 1, 1]
Выход: []

Вход: numbers = [0, 0, 0]
Выход: [[0, 0, 0]]
'''

from typing import List

def three_sum(numbers: List[int]) -> List[List[int]]:
    numbers.sort()
    result = []

    if len(numbers) < 3:
        return result

    for i in range(len(numbers)):
        if i > 0 and numbers[i] == numbers[i - 1]:
            continue

        left, right = i + 1, len(numbers) - 1
        while left < right:
            total = numbers[i] + numbers[left] + numbers[right]

            if total == 0:
                result.append([numbers[i], numbers[left], numbers[right]])
                left += 1
                right -= 1

                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1
                while left < right and numbers[right] == numbers[right + 1]:
                    right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return result