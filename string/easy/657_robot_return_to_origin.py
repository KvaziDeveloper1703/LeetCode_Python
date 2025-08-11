'''
A robot starts at the origin point (0, 0) on a 2D plane. It is given a sequence of moves represented by a string moves, where each character tells the robot which direction to move:
    + 'R' means move right,
    + 'L' means move left,
    + 'U' means move up,
    + 'D' means move down.
Each move changes the robot's position by exactly one unit in the specified direction.

Your task is to determine if, after performing all the moves in order, the robot returns to its starting position at (0, 0).

Return True if the robot ends up back at the origin, otherwise return False.

The robot's orientation does not matter — 'R' always moves it one unit to the right, and similarly for other directions.

Examples:
Input: moves = "UD"
Output: True

Input: moves = "LL"
Output: False

Робот начинает движение из начальной точки (0, 0) на двумерной плоскости. Задан порядок его движений в виде строки moves, где каждый символ означает шаг робота в одном из направлений:
    + 'R' — движение на одну единицу вправо,
    + 'L' — на одну единицу влево,
    + 'U' — на одну единицу вверх,
    + 'D' — на одну единицу вниз.
Все движения одинаковой длины и выполняются последовательно.

Ваша задача — определить, вернётся ли робот в исходную точку (0, 0) после выполнения всех шагов.

Необходимо вернуть True, если робот окажется в точке (0, 0) после всех движений, иначе вернуть False.

Направление, куда «смотрит» робот, не имеет значения — команды всегда перемещают его строго в указанную сторону.

Примеры:
Ввод: moves = "UD"
Вывод: True

Ввод: moves = "LL"
Вывод: False
'''

def judge_сircle(moves: str) -> bool:
    x, y = 0, 0

    for move in moves:
        if move == 'U':
            y += 1
        elif move == 'D':
            y -= 1
        elif move == 'R':
            x += 1
        elif move == 'L':
            x -= 1

    return x == 0 and y == 0