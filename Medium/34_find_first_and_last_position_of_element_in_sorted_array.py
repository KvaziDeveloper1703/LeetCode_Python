'''
You are given an array of integers numbers sorted in non-decreasing order. Your task is to find the starting and ending position of a given target value in the array.
If the target is not found, return [-1, -1].

You must implement an algorithm with O(log n) runtime complexity.

Examples:
Input: numbers = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: numbers = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Дан массив целых чисел numbers, отсортированный в неубывающем порядке. Необходимо найти начальную и конечную позицию заданного значения target в массиве.
Если target не найден, верните [-1, -1].

Реализуйте алгоритм с логарифмической сложностью — O(log n).

Примеры:
Ввод: numbers = [5,7,7,8,8,10], target = 8
Вывод: [3,4]

Ввод: numbers = [5,7,7,8,8,10], target = 6
Вывод: [-1,-1]
'''

from typing import List

def search_range(numbers: List[int], target: int) -> List[int]:
    def find_first(numbers, target):
        left, right = 0, len(numbers) - 1
        first = -1
        while left <= right:
            mid = (left + right) // 2
            if numbers[mid] == target:
                first = mid
                right = mid - 1
            elif numbers[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return first
    
    def find_last(numbers, target):
        left, right = 0, len(numbers) - 1
        last = -1
        while left <= right:
            mid = (left + right) // 2
            if numbers[mid] == target:
                last = mid
                left = mid + 1
            elif numbers[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return last
    
    return [find_first(numbers, target), find_last(numbers, target)]