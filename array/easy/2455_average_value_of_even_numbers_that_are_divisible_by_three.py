'''
You are given an integer array numbers consisting of positive integers.

Your task is to find the average value of all numbers in the array that satisfy both of the following conditions:
    - the number is even;
    - the number is divisible by 3.

The average of n elements is defined as the sum of these elements divided by n, rounded down to the nearest integer.

If there are no numbers that meet the conditions, return 0.

Examples:
Input: numbers = [1, 3, 6, 10, 12, 15]
Output: 9

Input: numbers = [1, 2, 4, 7, 10]
Output: 0

Дан массив целых положительных чисел numbers.

Необходимо найти среднее арифметическое всех чисел массива, которые удовлетворяют двум условиям:
    - число является чётным;
    - число делится на 3.

Среднее арифметическое n чисел вычисляется как сумма этих чисел, делённая на n, с округлением вниз до целого числа.

Если подходящих чисел нет, верните 0.

Примеры:
Ввод: numbers = [1, 3, 6, 10, 12, 15]
Вывод: 9

Ввод: numbers = [1, 2, 4, 7, 10]
Вывод: 0
'''

from typing import List

def average_value(numbers: List[int]) -> int:
    total_sum = 0
    count = 0

    for number in numbers:
        if number % 2 == 0 and number % 3 == 0:
            total_sum += number
            count += 1

    if count == 0:
        return 0

    return total_sum // count