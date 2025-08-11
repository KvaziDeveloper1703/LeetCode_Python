'''
Given an integer array numbers.

Return True if there exists a triple of indices (i, j, k) such that: i < j < k  and  numbers[i] < numbers[j] < numbers[k]. Otherwise, return False.

Examples:
Input: numbers = [1,2,3,4,5]
Output: True

Input: numbers = [5,4,3,2,1]
Output: False

Дан массив целых чисел numbers. 

Верните True, если существует тройка индексов (i, j, k) такая, что: i < j < k  и  numbers[i] < numbers[j] < numbers[k]. Если такой тройки не существует, верните False.

Примеры:
Ввод: numbers = [1,2,3,4,5]
Вывод: True

Ввод: numbers = [5,4,3,2,1]
Вывод: False
'''

from typing import List

def increasin_triplet(numbers: List[int]) -> bool:
    first_min = float('inf')
    second_min = float('inf')

    for number in numbers:
        if number <= first_min:
            first_min = number
        elif number <= second_min:
            second_min = number
        else:
            return True

    return False