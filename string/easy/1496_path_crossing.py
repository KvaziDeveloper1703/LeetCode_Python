'''
Given a string path, where each character represents a move on a 2D plane:
    + 'N' → move one unit north;
    + 'S' → move one unit south;
    + 'E' → move one unit east;
    + 'W' → move one unit west.

You start at the origin (0, 0) and follow the moves in path.

Return True if the path crosses itself at any point. Otherwise, return False.

Examples:
Input: path = "NES"
Output: False

Input: path = "NESWW"
Output: True

Дана строка path, где каждый символ задаёт шаг по координатной плоскости:
    + 'N' → шаг на одну единицу на север;
    + 'S' → шаг на одну единицу на юг;
    + 'E' → шаг на одну единицу на восток;
    + 'W' → шаг на одну единицу на запад.

Вы начинаете движение из точки (0, 0) и следуете по маршруту path.

Верните True, если маршрут пересекает сам себя в какой-либо момент. В противном случае верните False.

Примеры:
Ввод: path = "NES"
Вывод: False

Ввод: path = "NESWW"
Вывод: True
'''

def is_path_crossing(path: str) -> bool:
    x, y = 0, 0

    visited = {(0, 0)}

    for direction in path:
        if direction == 'N':
            y += 1
        elif direction == 'S':
            y -= 1
        elif direction == 'E':
            x += 1
        elif direction == 'W':
            x -= 1

        if (x, y) in visited:
            return True
        visited.add((x, y))

    return False