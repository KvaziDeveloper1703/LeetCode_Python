'''
Given an integer array array.

Return True if the array contains three consecutive odd numbers, and False otherwise.

Examples:
Input: array = [2,6,4,1]
Output: False

Input: array = [1,2,34,3,4,5,7,23,12]
Output: True

Дан массив целых чисел array.

Необходимо вернуть True, если в массиве есть три подряд идущих нечётных числа, и False - в противном случае.

Примеры:
Ввод: array = [2,6,4,1]
Вывод: False

Ввод: array = [1,2,34,3,4,5,7,23,12]
Вывод: True
'''

from typing import List

def three_consecutive_odds(array: List[int]) -> bool:
    count = 0
    for number in array:
        if number % 2 == 1:
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    return False