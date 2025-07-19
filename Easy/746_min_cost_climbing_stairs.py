'''
Given an integer array cost where cost[i] represents the cost of stepping on the i-th step of a staircase.
Once you pay the cost at a step, you can move either one step or two steps forward.
You can choose to start either at index 0 or index 1.

Return the minimum cost required to reach the top of the floor.

Examples:
Input: cost = [10, 15, 20]
Output: 15

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6

Вам дан массив целых чисел cost, где cost[i] — это стоимость наступления на i-ую ступень лестницы.
После оплаты стоимости за ступеньку вы можете подняться на одну или на две ступеньки вперёд.
Вы можете начать либо с нулевой, либо с первой ступеньки.

Ваша задача — вернуть минимальную стоимость, необходимую для того, чтобы достичь вершины лестницы.

Примеры:
Ввод: cost = [10, 15, 20]
Вывод: 15

Ввод: cost = [1,100,1,1,1,100,1,1,100,1]
Вывод: 6
'''

from typing import List

def min_cost_climbing_stairs(cost: List[int]) -> int:
    n = len(cost)
    cost_two_steps_before, cost_one_step_before = 0, 0

    for step in range(2, n + 1):
        current_cost = min(cost_one_step_before + cost[step - 1], cost_two_steps_before + cost[step - 2])
        cost_two_steps_before, cost_one_step_before = cost_one_step_before, current_cost

    return cost_one_step_before