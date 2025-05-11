'''
Given a list of non-negative integers numbers, arrange them such that they form the largest number possible and return it as a string.
Since the result can be very large, the return value must be a string, not an integer.

Examples:
Input: numbers = [10, 2]
Output: "210"

Input: numbers = [3, 30, 34, 5, 9]
Output: "9534330"

Дан список неотрицательных целых чисел numbers. Расположите числа так, чтобы в результате получилось наибольшее возможное число, и верните его в виде строки.
Так как результат может быть очень большим, его нужно вернуть в виде строки, а не числа.

Примеры:
Ввод: numbers = [10, 2]
Вывод: "210"

Ввод: numbers = [3, 30, 34, 5, 9]
Вывод: "9534330"
'''

def largest_number(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*10, reverse=True)

    if numbers[0] == "0":
        return "0"

    return ''.join(numbers)