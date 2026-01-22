'''
You are given an integer n, which represents the number of players in a game, and a 2D array pick, where pick[i] = [xᵢ, yᵢ] means that player xᵢ picked a ball of color yᵢ.

A player i wins if they pick strictly more than i balls of the same color. That means:
    - Player 0 wins if they pick at least 1 ball of any color;
    - Player 1 wins if they pick at least 2 balls of the same color;
    - Player 2 wins if they pick at least 3 balls of the same color;
    - ...
    - Player i wins if they pick at least (i + 1) balls of the same color.

Return the number of players who win the game.

Examples:
Input: n = 4, pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]
Output: 2

Input: n = 5, pick = [[1,1],[1,2],[1,3],[1,4]]
Output: 0

Дано целое число n, обозначающее количество игроков в игре, и двумерный массив pick, где pick[i] = [xᵢ, yᵢ] означает, что игрок xᵢ взял шарик цвета yᵢ.

Игрок i выигрывает, если он взял строго больше i шариков одного и того же цвета. То есть:
    - Игрок 0 выигрывает, если он взял хотя бы 1 шарик любого цвета;
    - Игрок 1 выигрывает, если он взял хотя бы 2 шарика одного цвета;
    - Игрок 2 выигрывает, если он взял хотя бы 3 шарика одного цвета;
    - ...
    - Игрок i выигрывает, если он взял хотя бы (i + 1) шариков одного цвета.

Верни количество игроков, которые выиграли.

Примеры:
Ввод: n = 4, pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]
Вывод: 2

Ввод: n = 5, pick = [[1,1],[1,2],[1,3],[1,4]]
Вывод: 0
'''

from typing import List
from collections import defaultdict

def winning_player_count(n: int, pick: List[List[int]]) -> int:
    player_color_count = defaultdict(lambda: defaultdict(int))

    for player, color in pick:
        player_color_count[player][color] += 1

    winners = 0

    for player in range(n):
        for count in player_color_count[player].values():
            if count > player:
                winners += 1
                break

    return winners