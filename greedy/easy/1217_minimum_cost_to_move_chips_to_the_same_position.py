'''
We have n chips, where the position of the i-th chip is given by position[i].

We need to move all the chips to the same position. In one step, we can:
    + Move the i-th chip from position[i] to position[i] + 2 or position[i] - 2 with cost = 0.
    + Move the i-th chip from position[i] to position[i] + 1 or position[i] - 1 with cost = 1.

Return the minimum cost required to move all the chips to the same position.

Examples:
Input: position = [1,2,3]
Output: 1

Input: position = [2,2,2,3,3]
Output: 2

Дано n фишек, где позиция i-й фишки указана в position[i].

Нужно переместить все фишки в одну и ту же позицию. За один шаг можно:
    + Переместить i-ю фишку из position[i] в position[i] + 2 или position[i] - 2 с стоимостью = 0.
    + Переместить i-ю фишку из position[i] в position[i] + 1 или position[i] - 1 с стоимостью = 1.

Верните минимальную стоимость, необходимую для того, чтобы собрать все фишки в одной позиции.

Примеры:
Ввод: position = [1,2,3]
Вывод: 1

Ввод: position = [2,2,2,3,3]
Вывод: 2
'''

from typing import List

def minimum_cost_to_move_chips(position: List[int]) -> int:
    even_count = sum(1 for p in position if p % 2 == 0)
    odd_count = len(position) - even_count
    return min(even_count, odd_count)