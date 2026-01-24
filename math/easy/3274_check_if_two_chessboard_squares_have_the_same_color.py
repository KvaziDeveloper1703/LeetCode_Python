'''
You are given two strings coordinate_1 and coordinate_2, each representing a square on an 8 × 8 chessboard.

Return True if the two squares have the same color, and False otherwise.

Each coordinate is always valid and follows this format:
    - the first character is a letter from 'a' to 'h',
    - the second character is a digit from '1' to '8'.

Examples:
Input: coordinate_1 = "a1", coordinate_2 = "c3"
Output: True

Input: coordinate_1 = "a1", coordinate_2 = "h3"
Output: False

Даны две строки coordinate_1 и coordinate_2, каждая из которых задаёт клетку на шахматной доске 8 × 8.

Нужно вернуть True, если обе клетки имеют одинаковый цвет, и False в противном случае.

Каждая координата всегда корректна и записывается в формате:
    - первая часть это буква от 'a' до 'h',
    - вторая часть это цифра от '1' до '8'.

Примеры:
Ввод: coordinate_1 = "a1", coordinate_2 = "c3"
Вывод: True

Ввод: coordinate_1 = "a1", coordinate_2 = "h3"
Вывод: False
'''

def check_two_chessboards(coordinate_1: str, coordinate_2: str) -> bool:
    column_1 = ord(coordinate_1[0]) - ord('a') + 1
    row_1 = int(coordinate_1[1])

    column_2 = ord(coordinate_2[0]) - ord('a') + 1
    row_2 = int(coordinate_2[1])

    return (column_1 + row_1) % 2 == (column_2 + row_2) % 2