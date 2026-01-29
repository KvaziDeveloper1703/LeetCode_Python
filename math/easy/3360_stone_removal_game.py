'''
Alice and Bob are playing a game with a pile of stones. They take turns removing stones from the pile, with Alice going first.
    - On her first turn, Alice must remove exactly 10 stones;
    - On each subsequent turn, the current player must remove exactly 1 fewer stone than the previous opponent removed;
    - If a player cannot make a move on their turn, that player loses the game.

You are given a positive integer n, representing the initial number of stones in the pile.

Return true if Alice wins the game assuming both players play optimally, and false otherwise.

Examples:
Input: n = 12
Output: true

Input: n = 1
Output: false

Алиса и Боб играют в игру с кучей камней. Они по очереди убирают камни из кучи, при этом Алиса ходит первой.
    - В свой первый ход Алиса должна убрать ровно 10 камней;
    - В каждый следующий ход игрок должен убрать на 1 камень меньше, чем убрал соперник на предыдущем ходе;
    - Если игрок не может сделать ход, он проигрывает.

Дано положительное целое число n, обозначающее начальное количество камней в куче.

Необходимо вернуть true, если Алиса выигрывает игру при оптимальной игре обоих игроков, и false в противном случае.

Примеры:
Ввод: n = 12
Вывод: true

Ввод: n = 1
Вывод: false
'''

def can_alice_win(n: int) -> bool:
    stones_left = n
    stones_to_remove = 10
    is_alice_turn = True

    while True:
        if stones_to_remove == 0 or stones_left < stones_to_remove:
            return not is_alice_turn

        stones_left -= stones_to_remove
        stones_to_remove -= 1
        is_alice_turn = not is_alice_turn