'''
You are given an array numbers consisting of positive integers.
    - The element sum is the sum of all elements in the array numbers;
    - The digit sum is the sum of all digits that appear in all numbers of the array.

Your task is to return the absolute difference between the element sum and the digit sum of numbers.

The absolute difference between two integers x and y is defined as |x - y|.

Examples:
Input: numbers = [1, 15, 6, 3]
Output: 9

Input: numbers = [1, 2, 3, 4]
Output: 0

Дан массив numbers, состоящий из положительных целых чисел.
Сумма элементов - это сумма всех чисел массива numbers;
Сумма цифр - это сумма всех цифр, входящих в числа массива.

Необходимо вернуть модуль разности между суммой элементов и суммой цифр массива numbers.

Модуль разности двух целых чисел x и y определяется как |x - y|.

Примеры:
Ввод: numbers = [1, 15, 6, 3]
Вывод: 9

Ввод: numbers = [1, 2, 3, 4]
Вывод: 0
'''

from typing import List

def difference_of_sum(numbers: List[int]) -> int:
    element_sum = sum(numbers)
    digit_sum = 0

    for number in numbers:
        for digit in str(number):
            digit_sum += int(digit)

    return abs(element_sum - digit_sum)