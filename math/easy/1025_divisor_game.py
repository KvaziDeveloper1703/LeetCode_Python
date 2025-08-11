'''
Alice and Bob take turns playing a game, with Alice going first.
    + Initially, there is a number n written on the chalkboard.
    + On each turn, the current player must:
        1) Choose a number x such that 0 < x < n and n % x == 0.
        2) Replace the number n on the chalkboard with n - x.
    + If a player cannot make a move, that player loses the game.

Return True if Alice will win the game assuming both players play optimally, otherwise return False.

Examples:
Input: n = 2
Output: True

Input: n = 3
Output: False

Алиса и Боб по очереди играют в игру, причём Алиса ходит первой.
    + Изначально на доске написано число n.
    + В свой ход игрок должен:
        1) Выбрать число x, такое что 0 < x < n и n % x == 0.
        2) Заменить число n на доске на n - x.
    + Если игрок не может сделать ход, он проигрывает.

Верните True, если Алиса выиграет при условии, что оба игрока играют оптимально, иначе верните False.

Примеры:
Ввод: n = 2
Вывод: True

Ввод: n = 3
Вывод: False
'''

def divisor_game(n: int) -> bool:
    return n % 2 == 0