'''
Given an integer n, return the least number of perfect square numbers that sum up to n.

A perfect square is an integer that is the square of another integer — in other words, it is the product of an integer with itself.
Examples of perfect squares: 1, 4, 9, 16; but 3 and 11 are not perfect squares.

Examples:
Input: n = 12
Output: 3

Input: n = 13
Output: 2

Дано целое число n. Требуется вернуть минимальное количество полных квадратов, сумма которых равна n.

Полный квадрат — это целое число, которое является квадратом другого целого числа.
Примеры полных квадратов: 1, 4, 9, 16 (так как 1², 2², 3², 4²), а вот 3 и 11 — не полные квадраты.

Примеры:
Ввод: n = 12
Вывод: 3

Ввод: n = 13
Вывод: 2
'''

def number_of_squares(self, n: int) -> int:
    min_number_of_squares = [float('inf')] * (n + 1)
    min_number_of_squares[0] = 0

    perfect_squares = [i * i for i in range(1, int(n ** 0.5) + 1)]

    for total in range(1, n + 1):
        for square in perfect_squares:
            if square > total:
                break
            min_number_of_squares[total] = min(min_number_of_squares[total], min_number_of_squares[total - square] + 1)

    return min_number_of_squares[n]