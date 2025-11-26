'''
You are given a string s of length n, consisting only of the characters 'X' and 'O'.

A move is defined as selecting any three consecutive characters in the string and converting all of them to 'O'. If a selected character is already 'O', it remains unchanged.

Return the minimum number of moves required to convert all characters in the string to 'O'.

Дана строка s длины n, состоящая только из символов 'X' и 'O'.

Ход - это выбор любых трёх подряд идущих символов строки и преобразование всех этих трёх символов в 'O'. Если какой-то из выбранных символов уже равен 'O', он остаётся таким.

Верните минимальное количество ходов, необходимое, чтобы преобразовать все символы строки в 'O'.
'''

def minimum_moves(s: str) -> int:
    moves_count = 0
    current_index = 0

    while current_index < len(s):
        if s[current_index] == 'X':
            moves_count += 1
            current_index += 3
        else:
            current_index += 1

    return moves_count