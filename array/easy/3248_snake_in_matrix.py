'''
There is a snake moving inside an n × n grid.
Each cell is labeled by its position: grid[i][j] = (i * n) + j.
The snake starts at cell 0 and then executes a sequence of commands.

You are given:
    - an integer n (size of the grid);
    - an array of strings commands, where each command is one of: "UP", "RIGHT", "DOWN", "LEFT".

It is guaranteed that the snake will never leave the grid.
Return the number of the final cell where the snake ends up after executing all commands.

Examples:
Input: n = 2, commands = ["RIGHT", "DOWN"]
Output: 3

Input: n = 3, commands = ["DOWN", "RIGHT", "UP"]
Output: 1

В квадратной сетке n × n движется змейка.
Каждая клетка имеет номер по формуле: grid[i][j] = (i * n) + j.
Змейка начинает в клетке 0 и затем выполняет последовательность команд.

Вам даны:
    - целое число n (размер сетки);
    - массив строк commands, где каждая команда одна из: "UP", "RIGHT", "DOWN", "LEFT".

Гарантируется, что змейка никогда не выйдет за пределы сетки.
Верните номер конечной клетки, в которой окажется змейка после выполнения всех команд.

Примеры:
Input: n = 2, commands = ["RIGHT", "DOWN"]
Output: 3

Input: n = 3, commands = ["DOWN", "RIGHT", "UP"]
Output: 1
'''

from typing import List

def final_position_of_snake(n: int, commands: List[str]) -> int:
    row = 0
    column = 0

    for command in commands:
        if command == "UP":
            row -= 1
        elif command == "DOWN":
            row += 1
        elif command == "LEFT":
            column -= 1
        else:
            column += 1

    return row * n + column