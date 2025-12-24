'''
Given an array of positive integers numbers, return an array answer that contains all the digits of each integer in numbers, separated and placed in the same order as they appear in numbers.

Separating the digits of an integer means extracting each digit individually while preserving their original order.

Examples:
Input: numbers = [13, 25, 83, 77]
Output: [1, 3, 2, 5, 8, 3, 7, 7]

Input: numbers = [7, 1, 3, 9]
Output: [7, 1, 3, 9]

Дан массив положительных целых чисел numbers. Необходимо вернуть массив answer, который содержит все цифры каждого числа из numbers, разделённые и расположенные в том же порядке, в котором они встречаются в массиве numbers.

Разделить число на цифры означает получить все его цифры по порядку слева направо.

Примеры:
Ввод: numbers = [13, 25, 83, 77]
Вывод: [1, 3, 2, 5, 8, 3, 7, 7]

Ввод: numbers = [7, 1, 3, 9]
Вывод: [7, 1, 3, 9]
'''

def separate_digits(numbers):
    result = []
    for number in numbers:
        for digit in str(number):
            result.append(int(digit))
    return result