'''
You are given an array numbers consisting of positive integers.
The frequency of an element is defined as the number of times that element appears in the array.
Your task is to find the maximum frequency among all elements in the array and then return the total number of occurrences of all elements that have this maximum frequency.

Examples:
Input: numbers = [1,2,2,3,1,4]
Output: 4

Input: numbers = [1,2,3,4,5]
Output: 5

Дан массив numbers, состоящий из положительных целых чисел.
Частота элемента - это количество раз, которое данный элемент встречается в массиве.
Необходимо определить максимальную частоту среди всех элементов массива, а затем вернуть общее количество вхождений всех элементов, которые имеют эту максимальную частоту.

Примеры:
Ввод: numbers = [1,2,2,3,1,4]
Вывод: 4

Ввод: numbers = [1,2,3,4,5]
Вывод: 5
'''

from typing import List
from collections import Counter

def max_frequency_elements(numbers: List[int]) -> int:
    frequency_map = Counter(numbers)
    maximum_frequency = max(frequency_map.values())

    total_count = 0
    for frequency in frequency_map.values():
        if frequency == maximum_frequency:
            total_count += frequency

    return total_count