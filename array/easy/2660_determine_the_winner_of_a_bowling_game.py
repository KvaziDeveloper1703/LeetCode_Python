'''
You are given two 0-indexed integer arrays player1 and player2, where each array represents the number of pins knocked down by Player 1 and Player 2 in a bowling game.

The bowling game consists of n turns, and in each turn there are exactly 10 pins.

Let xᵢ be the number of pins a player knocks down in the i-th turn.

The score for the i-th turn is calculated as follows:
    - If the player knocked down 10 pins in either the (i − 1)-th or (i - 2)-th turn, then the value of the current turn is 2 × xᵢ;
    - Otherwise, the value of the current turn is xᵢ.

The total score of a player is the sum of the values of all their turns.

Your task is to:
    - Return 1 if Player 1’s score is greater than Player 2’s score;
    - Return 2 if Player 2’s score is greater than Player 1’s score;
    - Return 0 if both players have the same score.

Examples:
Input: player1 = [5, 10, 3, 2], player2 = [6, 5, 7, 3]
Output: 1

Input: player1 = [3, 5, 7, 6], player2 = [8, 10, 10, 2]
Output: 2

Вам даны два целочисленных массива с нулевой индексацией player1 и player2, где каждый массив представляет количество кеглей, сбитых игроком 1 и игроком 2 в игре в боулинг.

Игра состоит из n ходов, и в каждом ходе на дорожке находится ровно 10 кеглей.

Пусть xᵢ - количество кеглей, сбитых игроком на i-м ходе.

Очки за i-й ход рассчитываются следующим образом:
    - Если игрок сбил 10 кеглей на (i − 1)-м или (i − 2)-м ходе, то очки за текущий ход равны 2 × xᵢ;
    - В противном случае очки за ход равны xᵢ.

Общий счёт игрока - это сумма очков за все его ходы.

Необходимо:
    - Вернуть 1, если счёт первого игрока больше счёта второго;
    - Вернуть 2, если счёт второго игрока больше счёта первого;
    - Вернуть 0, если счёты равны.

Примеры:
Ввод: player1 = [5, 10, 3, 2], player2 = [6, 5, 7, 3]
Вывод: 1

Ввод: player1 = [3, 5, 7, 6], player2 = [8, 10, 10, 2]
Вывод: 2
'''

from typing import List

def is_winner(player1: List[int], player2: List[int]) -> int:
    def calculate_score(player: List[int]) -> int:
        total_score = 0

        for turn_index in range(len(player)):
            if ((turn_index >= 1 and player[turn_index - 1] == 10) or (turn_index >= 2 and player[turn_index - 2] == 10)):
                total_score += 2 * player[turn_index]
            else:
                total_score += player[turn_index]

        return total_score

    player1_score = calculate_score(player1)
    player2_score = calculate_score(player2)

    if player1_score > player2_score:
        return 1
    elif player2_score > player1_score:
        return 2
    else:
        return 0