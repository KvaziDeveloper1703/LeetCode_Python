'''
You are given a sorted array of distinct integers and a target value. Return the index if the target is found. 
If it is not found, return the index where it would be inserted in order to maintain the array's sorted order.

You must implement an algorithm with O(log n) runtime complexity.

Examples:
Input: numbers = [1,3,5,6], target = 5
Output: 2

Input: numbers = [1,3,5,6], target = 2
Output: 1

Дан отсортированный массив различных целых чисел и значение target. Необходимо вернуть индекс, если target найден. 
Если нет, вернуть индекс, куда его можно вставить, чтобы сохранить порядок сортировки массива.

Реализуйте алгоритм с логарифмической сложностью — O(log n).

Примеры:
Ввод: numbers = [1,3,5,6], target = 5
Вывод: 2

Ввод: numbers = [1,3,5,6], target = 2
Вывод: 1
'''

from typing import List

def search_insert(numbers: List[int], target: int) -> int:
    left, right = 0, len(numbers) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left