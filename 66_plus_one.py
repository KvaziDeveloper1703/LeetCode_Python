'''
You are given a large integer represented as an array digits, where each digits[i] is a digit of the number, ordered from most significant to least significant (left to right). The number has no leading zeros.
Increment the integer by one and return the resulting array of digits.

Example:
Input: digits = [1,2,3]
Output: [1,2,4]

Дан большой целый число в виде массива digits, где digits[i] — это цифра числа. Цифры расположены от старших к младшим (слева направо), и в числе нет ведущих нулей.
Увеличьте число на единицу и верните массив цифр результата.

Пример:
Ввод: digits = [1,2,3]
Вывод: [1,2,4]
'''

from typing import List

def plus_one(digits: List[int]) -> List[int]:
    index = len(digits) - 1

    while index >= 0:
        if digits[index] < 9:
            digits[index] += 1
            return digits
        else:
            digits[index] = 0
            index -= 1
    
    digits.insert(0, 1)
    return digits