'''
You are given an integer array numbers that is sorted in ascending order with distinct values, but it may have been rotated at an unknown pivot index k (where 1 ≤ k < numbers.length). 
The rotation means the array was split at some point and the two parts were swapped. For example, the array [0,1,2,4,5,6,7] might be rotated at index 3 and become [4,5,6,7,0,1,2].

Given the rotated array numbers and an integer target, return the index of target if it exists in the array, otherwise return -1.
You must design an algorithm that runs in O(log n) time.

Examples:
Input: numbers = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: numbers = [4,5,6,7,0,1,2], target = 3
Output: -1

Дан массив целых чисел numbers, который был отсортирован по возрастанию и содержит уникальные элементы, но мог быть повёрнут вокруг некоторого неизвестного индекса k (где 1 ≤ k < numbers.length). 
Это означает, что массив был разделён на две части, и они поменялись местами. Например, массив [0,1,2,4,5,6,7] мог быть повёрнут в точке 3 и стать [4,5,6,7,0,1,2].

Ваша задача — по данному массиву numbers и числу target вернуть индекс target, если он есть в массиве, или -1, если его нет.
Необходимо реализовать алгоритм с логарифмической сложностью — O(log n).

Примеры:
Ввод: numbers = [4,5,6,7,0,1,2], target = 0
Вывод: 4

Ввод: numbers = [4,5,6,7,0,1,2], target = 3
Вывод: -1
'''

from typing import List

def search(numbers: List[int], target: int) -> int:
    left, right = 0, len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle
        if numbers[left] <= numbers[middle]:
            if numbers[left] <= target < numbers[middle]:
                right = middle - 1
            else:
                left = middle + 1
        else:
            if numbers[middle] < target <= numbers[right]:
                left = middle + 1
            else:
                right = middle - 1
    return -1