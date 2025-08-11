'''
You are climbing a staircase. It takes n steps to reach the top.
Each time, you can either climb 1 step or 2 steps. 
In how many distinct ways can you climb to the top?

Examples:
Input: n = 2
Output: 2

Input: n = 3
Output: 3

Вы поднимаетесь по лестнице, состоящей из n ступеней.
За один шаг вы можете подняться либо на 1 ступень, либо на 2 ступени.
Сколько существует различных способов добраться до вершины лестницы?

Примеры:
Ввод: n = 2
Вывод: 2

Ввод: n = 3
Вывод: 3
'''

def climb_stairs(n: int) -> int:
    if n == 1:
        return 1

    previous_2, previous_1 = 1, 1

    for i in range(2, n + 1):
        current = previous_1 + previous_2
        previous_2 = previous_1
        previous_1 = current

    return previous_1