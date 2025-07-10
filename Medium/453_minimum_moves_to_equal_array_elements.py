'''
Given an integer array numbers of length n. In one move, you can increment n - 1 elements of the array by 1. 

Return the minimum number of moves required to make all elements in the array equal.

Examples:
Input: numbers = [1, 2, 3]
Output: 3

Input: numbers = [1,1,1]
Output: 0

Дан массив целых чисел numbers длины n. За один ход можно увеличить на 1 ровно n - 1 элементов массива.

Требуется найти минимальное количество ходов, чтобы все элементы массива стали равны.

Примеры:
Ввод: numbers = [1, 2, 3]
Вывод: 3

Ввод: numbers = [1,1,1]
Вывод: 0
'''

def minimum_moves(numbers: list[int]) -> int:
    minimum_number = min(numbers)
    moves = sum(number - minimum_number for number in numbers)
    return moves