'''
Given a non-empty array of non-negative integers numbers, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a contiguous subarray of numbers that has the same degree as numbers.

Examples:
Input: numbers = [1,2,2,3,1]
Output: 2

Input: numbers = [1,2,2,3,1,4,2]
Output: 6

Дан непустой массив неотрицательных целых чисел numbers. Степенью массива называется максимальная частота появления какого-либо одного элемента в массиве.

Ваша задача — найти минимально возможную длину непрерывной подмассива массива numbers, который имеет такую же степень, как и весь массив.

Примеры:
Ввод: numbers = [1,2,2,3,1]
Вывод: 2

Ввод: numbers = [1,2,2,3,1,4,2]
Вывод: 6
'''

from collections import defaultdict

def find_shortest_sub_array(numbers: List[int]) -> int:
    left = {}
    right = {}
    count = defaultdict(int)

    for i, number in enumerate(numbers):
        if number not in left:
            left[number] = i
        right[number] = i
        count[number] += 1

    degree = max(count.values())
    min_length = len(numbers)

    for number in count:
        if count[number] == degree:
            min_length = min(min_length, right[number] - left[number] + 1)

    return min_length