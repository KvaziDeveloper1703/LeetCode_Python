'''
You are given n coins and want to arrange them into a staircase shape.
The staircase consists of k rows, where the i-th row contains exactly i coins.

This means:
    - Row 1 has 1 coin
    - Row 2 has 2 coins
    - Row 3 has 3 coins, and so on.

The last row may be incomplete if there are not enough coins to fill it completely.
Your task is to determine how many rows of the staircase can be completed using n coins.
Return the number of complete rows.

Examples:
Input: n = 5
Output: 2

Input: n = 8
Output: 3

У вас есть n монет, и вы хотите выложить из них лестницу.
Лестница состоит из k рядов, где в i-м ряду находится ровно i монет.

То есть:
    - 1-й ряд содержит 1 монету
    - 2-й ряд содержит 2 монеты
    - 3-й ряд содержит 3 монеты и так далее.

Последний ряд может быть неполным, если монет недостаточно, чтобы заполнить его полностью.
Необходимо определить, сколько рядов лестницы можно полностью построить из n монет.
Верните количество полностью заполненных рядов.

Примеры:
Ввод: n = 5
Вывод: 2

Ввод: n = 8
Вывод: 3
'''

def arrange_coins(n: int) -> int:
    row = 1
    while n >= row:
        n -= row
        row += 1
    return row - 1