'''
Given an integer array numbers, find three numbers in the array whose product is the maximum possible, and return that maximum product.

Examples:
Input: numbers = [1,2,3]
Output: 6

Input: numbers = [1,2,3,4]
Output: 24

Дан массив целых чисел numbers. Найдите три числа в массиве, произведение которых будет максимальным возможным, и верните это максимальное произведение.

Примеры:
Ввод: numbers = [1,2,3]
Вывод: 6

Ввод: numbers = [1,2,3,4]
Вывод: 24
'''

from typing import List

def maximum_product(numbers: List[int]) -> int:
    max1 = max2 = max3 = float('-inf')
    min1 = min2 = float('inf')
    
    for number in numbers:
        if number > max1:
            max3 = max2
            max2 = max1
            max1 = number
        elif number > max2:
            max3 = max2
            max2 = number
        elif number > max3:
            max3 = number
        
        if number < min1:
            min2 = min1
            min1 = number
        elif number < min2:
            min2 = number
    
    product1 = max1 * max2 * max3
    product2 = min1 * min2 * max1
    
    return max(product1, product2)