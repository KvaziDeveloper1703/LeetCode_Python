"""
In the "100 game", two players take turns adding numbers to a running total. Each player can choose any integer from 1 to 10, and the player who makes the total reach or exceed 100 wins.

Now, imagine a variation of the game:
    + Players cannot reuse numbers — once a number is picked, it’s removed from the pool;
    + The pool consists of all integers from 1 to max_choosable_integer;
    + Players take turns picking unused numbers from the pool and adding them to the running total;
    + The first player to make the total reach or exceed desired_total wins.

Given two integers max_choosable_integer and desired_total, return True if the first player can force a win, assuming both players play optimally. Otherwise, return False.

Examples:
Input: max_choosable_integer = 10, desired_total = 11
Output: False

Input: max_choosable_integer = 10, desired_total = 0
Output: True

В классической игре "100" два игрока по очереди добавляют к общей сумме числа от 1 до 10. Побеждает тот, кто первым доведёт сумму до 100 или больше.

В изменённой версии игры:
    + Каждое число можно выбрать только один раз.
    + Игроки берут числа по очереди из общего набора от 1 до max_choosable_integer.
    + После выбора число удаляется из набора.
    + Цель — достичь или превысить desired_total.

Побеждает тот, кто первый достигнет этой цели.

Вам даны два числа: max_choosable_integer и desired_total. Верните True, если первый игрок может гарантированно победить, если оба играют оптимально. Иначе верните False.

Примеры:
Ввод: max_choosable_integer = 10, desired_total = 11
Вывод: False

Ввод: max_choosable_integer = 10, desired_total = 0
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