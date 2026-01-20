'''
You are playing the Nim Game with your friend:
    - At the beginning, there is a heap of n stones on the table;
    - You and your friend take turns, and you go first;
    - On each turn, a player removes 1 to 3 stones from the heap;
    - The player who removes the last stone wins.

Given an integer n, return true if you can win the game assuming both players play optimally, otherwise return false.

Examples:
Input: n = 4
Output: false

Input: n = 1
Output: true

Вы играете с другом в игру Nim:
    - В начале на столе лежит куча из n камней;
    - Вы ходите по очереди, и первый ход делаете вы;
    - За один ход игрок может убрать от 1 до 3 камней;
    - Побеждает тот, кто забирает последний камень.

Дано целое число n. Верните true, если вы можете выиграть при оптимальной игре обоих игроков, иначе верните false.

Примеры:
Ввод: n = 4
Вывод: false

Ввод: n = 1
Вывод: true
'''

def can_win_nim(n: int) -> bool:
    return n % 4 != 0