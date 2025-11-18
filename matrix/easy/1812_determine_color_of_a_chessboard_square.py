'''
You are given a string coordinates representing a square on a chessboard.
The string always has a letter first and a digit second, and it always refers to a valid square.

Return True if the square is white, and False if the square is black.

Examples:
Input: coordinates = "a1"
Output: False

Input: coordinates = "h3"
Output: True

Дана строка coordinates, которая обозначает клетку на шахматной доске.
Строка всегда содержит сначала букву, а затем цифру, и всегда является корректной координатой.

Нужно вернуть True, если клетка белая, и False, если клетка чёрная.

Примеры:
Ввод: coordinates = "a1"
Вывод: False

Ввод: coordinates = "h3"
Вывод: True
'''

def square_is_white(coordinates: str) -> bool:
    column_letter = coordinates[0]
    row_number = coordinates[1]

    column_index = ord(column_letter) - ord('a') + 1
    row_index = int(row_number)

    return (column_index + row_index) % 2 == 1