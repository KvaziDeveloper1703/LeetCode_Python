'''
Given an array of integers numbers which is sorted in ascending order, and an integer target, write a function to search for target in numbers. If target exists, return its index. Otherwise, return -1.
You must implement an algorithm with O(log n) runtime complexity.

Examples:
Input: numbers = [-1,0,3,5,9,12], target = 9
Output: 4

Input: numbers = [-1,0,3,5,9,12], target = 2
Output: -1

Дан массив целых чисел numbers, отсортированный по возрастанию, и целое число target. Напишите функцию для поиска target в numbers. Если target существует, верните его индекс. В противном случае верните -1.
Необходимо реализовать алгоритм с асимптотикой O(log n) по времени.

Примеры:
Ввод: numbers = [-1,0,3,5,9,12], target = 9
Вывод: 4

Ввод: numbers = [-1,0,3,5,9,12], target = 2
Вывод: -1
'''

def search(numbers: List[int], target: int) -> int:
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = left + (right - left) // 2
        if numbers[middle] == target:
            return middle
        elif numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1