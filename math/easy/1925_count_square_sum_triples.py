'''
A square triple (a,b,c) is a triple of integers where the square of a plus the square of b is equal to the square of c.

Given an integer n, return how many square triples exist such that all three numbers a, b, and c are between 1 and n inclusive.

Examples:
Input: n = 5
Output: 2

Input: n = 10
Output: 4

Квадратная тройка (a,b,c) - это набор из трёх целых чисел, где квадрат числа a плюс квадрат числа b равен квадрату числа c.

Дано целое число n. Нужно определить, сколько таких троек существует, при условии что a, b и c находятся в диапазоне от 1 до n включительно.

Примеры:
Ввод: n = 5
Вывод: 2

Ввод: n = 10
Вывод: 4
'''

def count_triples(number_limit: int) -> int:
    triple_count = 0

    for first_value in range(1, number_limit + 1):
        for second_value in range(1, number_limit + 1):
            sum_of_squares = first_value * first_value + second_value * second_value
            third_value = int(sum_of_squares ** 0.5)

            if third_value * third_value == sum_of_squares and third_value <= number_limit:
                triple_count += 1

    return triple_count