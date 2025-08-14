'''
Given an integer array numbers. Find a subsequence of numbers such that:
    + The sum of its elements is strictly greater than the sum of the elements that are not included in it;
    + If there are multiple such subsequences, choose the one with the minimum size;
    + If there are still multiple options, choose the one with the maximum total sum.

A subsequence can be obtained by removing zero or more elements from the array without changing the order of the remaining elements. The answer is guaranteed to be unique under these conditions. Return the subsequence sorted in non-increasing order.

Examples:
Input: numbers = [4,3,10,9,8]
Output: [10,9]

Input: numbers = [4,4,7,6,7]
Output: [7,7,6]

Дан массив целых чисел numbers. Найдите подпоследовательность этого массива, такую что:
    + Сумма её элементов строго больше суммы элементов, которые в неё не входят;
    + Если таких подпоследовательностей несколько, выберите ту, у которой минимальный размер;
    + Если и при этом останется несколько вариантов, выберите ту, у которой наибольшая сумма элементов.

Подпоследовательность можно получить, удалив из массива ноль или больше элементов, не меняя порядок оставшихся. При данных условиях ответ гарантированно единственный. Верните подпоследовательность, отсортированную по невозрастанию.

Примеры:
Ввод: numbers = [4,3,10,9,8]
Вывод: [10,9]

Ввод: numbers = [4,4,7,6,7]
Вывод: [7,7,6]
'''

from typing import List

def min_subsequence(numbers: List[int]) -> List[int]:
    numbers.sort(reverse=True)
    total = sum(numbers)
    picked_sum = 0
    result = []
    for x in numbers:
        result.append(x)
        picked_sum += x
        if picked_sum > total - picked_sum:
            break
    return result