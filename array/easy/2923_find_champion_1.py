'''
There are n teams in a tournament, numbered from 0 to n - 1.

You are given a 0-indexed 2D boolean matrix grid of size n × n.

For any two different teams i and j (0 ≤ i, j ≤ n - 1, i ≠ j):
    - if grid[i][j] == 1, then team i is stronger than team j;
    - otherwise, team j is stronger than team i.

A team a is the champion of the tournament if there is no other team b that is stronger than team a.

Return the index of the team that will be the champion of the tournament.

Examples:
Input: grid = [[0,1],[0,0]]
Output: 0

Input: grid = [[0,0,1],[1,0,1],[0,0,0]]
Output: 1

В турнире участвуют n команд, пронумерованных от 0 до n - 1.

Дана двумерная булева матрица grid размера n × n с индексацией с нуля.

Для любых двух различных команд i и j (0 ≤ i, j ≤ n - 1, i ≠ j) выполняется:
    - если grid[i][j] == 1, то команда i сильнее команды j;
    - иначе команда j сильнее команды i.

Команда a становится чемпионом турнира, если не существует другой команды b, которая сильнее команды a.

Верните номер команды, которая станет чемпионом турнира.

Примеры:
Ввод: grid = [[0,1],[0,0]]
Вывод: 0

Ввод: grid = [[0,0,1],[1,0,1],[0,0,0]]
Вывод: 1
'''

from typing import List

def find_сhampion(grid: List[List[int]]) -> int:
    number_of_teams = len(grid)

    for team_index in range(number_of_teams):
        is_champion = True

        for opponent_index in range(number_of_teams):
            if team_index != opponent_index and grid[opponent_index][team_index] == 1:
                is_champion = False
                break

        if is_champion:
            return team_index

    return -1