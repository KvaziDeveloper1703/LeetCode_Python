'''
Given a positive integer number, return True if number is a perfect square, otherwise return False.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

Examples:
Input: number = 16
Output: True

Input: number = 14
Output: False

Дано положительное целое число number. Верните True, если number является полным квадратом, иначе верните False.

Полный квадрат - это число, которое можно представить как квадрат целого числа, то есть как произведение некоторого целого числа само на себя.

Примеры:
Ввод: number = 16
Вывод: True

Ввод: number = 14
Вывод: False
'''

def is_perfect_square(number: int) -> bool:
    left = 1
    right = number

    while left <= right:
        middle = (left + right) // 2
        square = middle * middle

        if square == number:
            return True
        elif square < number:
            left = middle + 1
        else:
            right = middle - 1

    return False