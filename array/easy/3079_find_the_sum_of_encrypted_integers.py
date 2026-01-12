'''
You are given an integer array numbers consisting of positive integers.
We define a function encrypt(x) as follows: encrypt(x) replaces every digit in the number x with the largest digit present in x.
Apply the encrypt function to every element of the array numbers and return the sum of all encrypted elements.

Examples:
Input: numbers = [1, 2, 3]
Output: 6

Input: numbers = [10, 21, 31]
Output: 66

Вам дан целочисленный массив numbers, состоящий из положительных чисел.
Определим функцию encrypt(x) следующим образом: encrypt(x) заменяет каждую цифру числа x на наибольшую цифру, содержащуюся в этом числе.
Примените функцию encrypt ко всем элементам массива numbers и верните сумму всех зашифрованных элементов.

Примеры:
Ввод: numbers = [1, 2, 3]
Вывод: 6

Ввод: numbers = [10, 21, 31]
Вывод: 66
'''

from typing import List

def sum_of_encrypted_int(numbers: List[int]) -> int:
    total_sum = 0

    for number in numbers:
        digits = list(str(number))
        maximum_digit = max(digits)
        encrypted_number = int(maximum_digit * len(digits))
        total_sum += encrypted_number

    return total_sum