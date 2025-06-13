"""
In the "100 game", two players take turns adding numbers to a running total. Each player can choose any integer from 1 to 10, and the player who makes the total reach or exceed 100 wins.

Now, imagine a variation of the game:
    + Players cannot reuse numbers — once a number is picked, it’s removed from the pool.
    + The pool consists of all integers from 1 to maxChoosableInteger.
    + Players take turns picking unused numbers from the pool and adding them to the running total.
    + The first player to make the total reach or exceed desiredTotal wins.

Given two integers maxChoosableInteger and desiredTotal, return true if the first player can force a win, assuming both players play optimally. Otherwise, return false.

Examples:
Input: maxChoosableInteger = 10, desiredTotal = 11
Output: false

Input: maxChoosableInteger = 10, desiredTotal = 0
Output: true

В классической игре "100" два игрока по очереди добавляют к общей сумме числа от 1 до 10. Побеждает тот, кто первым доведёт сумму до 100 или больше.

В изменённой версии игры:
    + Каждое число можно выбрать только один раз.
    + Игроки берут числа по очереди из общего набора от 1 до maxChoosableInteger.
    + После выбора число удаляется из набора.
    + Цель — достичь или превысить desiredTotal.

Побеждает тот, кто первый достигнет этой цели.

Вам даны два числа: maxChoosableInteger и desiredTotal.
Верните true, если первый игрок может гарантированно победить, если оба играют оптимально. Иначе верните false.

Примеры:
Ввод: maxChoosableInteger = 10, desiredTotal = 11
Вывод: false

Ввод: maxChoosableInteger = 10, desiredTotal = 0
Вывод: true
"""

def can_i_win(max_choosable_integer: int, desired_total: int) -> bool:
    if (max_choosable_integer * (max_choosable_integer + 1)) // 2 < desired_total:
        return False
    if desired_total == 0:
        return True

    memo = {}

    def can_win(used, total):
        if used in memo:
            return memo[used]

        for i in range(1, max_choosable_integer + 1):
            current_bit = 1 << (i - 1)
            if used & current_bit:
                continue
            if i >= total or not can_win(used | current_bit, total - i):
                memo[used] = True
                return True

        memo[used] = False
        return False

    return can_win(0, desired_total)