'''
You are given a 0-indexed integer array numbers.

The concatenation of two numbers is defined as the number obtained by joining their digits together.

The concatenation value of numbers is initially set to 0. Repeat the following operation until the array numbers becomes empty:
    - If numbers contains more than one element, take the first and the last elements, concatenate them, add the resulting number to the concatenation value, and then remove both elements from numbers;
    - If numbers contains exactly one element, add its value to the concatenation value and then remove it from numbers.

Return the final concatenation value of numbers.

Examples:
Input: numbers = [7, 52, 2, 4]
Output: 596

Input: numbers = [5, 14, 13, 8, 12]
Output: 673

Дан целочисленный массив numbers, проиндексированный с нуля.

Конкатенацией двух чисел называется число, полученное путём приписывания цифр второго числа к цифрам первого.

Конкатенационное значение массива numbers изначально равно 0. Необходимо выполнять следующую операцию, пока массив numbers не станет пустым:
    - Если в массиве numbers больше одного элемента, взять первый и последний элементы, выполнить их конкатенацию, добавить полученное число к конкатенационному значению и удалить оба элемента из массива;
    - Если в массиве numbers остался ровно один элемент, добавить его значение к конкатенационному значению и затем удалить его из массива.

Необходимо вернуть итоговое конкатенационное значение массива numbers.

Примеры:
Ввод: numbers = [7, 52, 2, 4]
Вывод: 596

Ввод: numbers = [5, 14, 13, 8, 12]
Вывод: 673
'''

from typing import List

def find_the_array_concatenation_value(numbers: List[int]) -> int:
    left_index = 0
    right_index = len(numbers) - 1
    concatenation_value = 0

    while left_index <= right_index:
        if left_index == right_index:
            concatenation_value += numbers[left_index]
        else:
            concatenated_number = int(str(numbers[left_index]) + str(numbers[right_index]))
            concatenation_value += concatenated_number

        left_index += 1
        right_index -= 1

    return concatenation_value