'''
Given an array numbers of non-negative integers.

An array is called special if there exists a number X such that exactly X numbers in numbers are greater than or equal to X.

Note:
    + X does not need to be an element of numbers;
    + If the array is special, the value of X is guaranteed to be unique.

Return X if the array is special, otherwise return -1.

Examples:
Input: numbers = [3, 5]  
Output: 2

Input: numbers = [0, 0]  
Output: -1

Дан массив numbers, состоящий из неотрицательных целых чисел.

Массив называется особым, если существует число X такое, что ровно X чисел в массиве numbers больше либо равны X.

Замечания:
    + X не обязан быть элементом массива numbers;
    + Если массив является особым, то значение X гарантированно единственное.

Верните X, если массив особый, иначе верните -1.

Примеры:
Ввод: numbers = [3, 5]  
Вывод: 2  

Ввод: numbers = [0, 0]  
Вывод: -1
'''

from typing import List

def special_array(numbers: List[int]) -> int:
    n = len(numbers)

    for x in range(0, n + 1):
        count = 0
        for number in numbers:
            if number >= x:
                count += 1
        if count == x:
            return x

    return -1