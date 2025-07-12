'''
There are n bulbs that are initially off.
    + In the first round, you turn on all the bulbs;
    + In the second round, you turn off every second bulb;
    + In the third round, you toggle every third bulb (turning it on if it is off, or turning it off if it is on);
    + In the ith round, you toggle every ith bulb;
    + In the nth round, you only toggle the last bulb.

Return the number of bulbs that are on after n rounds.

Examples:
Input: n = 3
Output: 1

Input: n = 0
Output: 0

Есть n лампочек, которые изначально выключены.
    + В первом раунде вы включаете все лампочки;
    + Во втором раунде вы выключаете каждую вторую лампочку;
    + В третьем раунде вы переключаете каждую третью лампочку (если она была выключена — включаете, если включена — выключаете);
    + В i-ом раунде вы переключаете каждую i-ю лампочку;
    + В n-ом раунде вы переключаете только последнюю лампочку.

Нужно вернуть количество лампочек, которые останутся включёнными после n раундов.

Примеры:
Ввод: n = 3
Вывод: 1

Ввод: n = 0
Вывод: 0
'''

def bulb_switch(n: int) -> int:
    bulbs = [False] * n

    for round_number in range(1, n + 1):
        for i in range(round_number - 1, n, round_number):
            bulbs[i] = not bulbs[i]

    return sum(bulbs)