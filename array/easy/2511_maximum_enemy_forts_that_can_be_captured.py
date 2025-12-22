'''
You are given a 0-indexed integer array forts of length n, which represents the positions of several forts.

Each element of the array can have one of the following values:
    - -1 - there is no fort at this position,
    - 0 - there is an enemy fort at this position,
    - 1 - there is a fort under your command at this position.

You want to move your army from one of your own forts at position i to an empty position j, subject to the following conditions:
    - 0 ≤ i, j ≤ n - 1;
    - The army moves only through enemy forts. Formally, for every index k such that min(i, j) < k < max(i, j), it must hold that forts[k] == 0.

While the army is moving, all enemy forts along the path are captured.

Return the maximum number of enemy forts that can be captured in a single move.

If it is impossible to move the army, or if you do not have any fort under your command, return 0.

Examples:
Input:  forts = [1,0,0,-1,0,0,0,0,1]
Output: 4

Input:  forts = [0,0,1,-1]
Output: 0

Дан целочисленный массив forts, индексированный с нуля, длины n, который описывает расположение нескольких фортов.

Каждый элемент массива может принимать одно из следующих значений:
    - -1 - в данной позиции нет форта,
    - 0 - в данной позиции находится вражеский форт,
    - 1 - в данной позиции находится форт под вашим командованием.

Вы хотите переместить армию из одного своего форта в позиции i в пустую позицию j при выполнении следующих условий:
    - 0 ≤ i, j ≤ n - 1;
    - Армия может проходить только через вражеские форты. Формально, для любого индекса k, такого что min(i, j) < k < max(i, j), должно выполняться forts[k] == 0.

Во время движения армии все вражеские форты на пути захватываются.

Необходимо вернуть максимальное количество вражеских фортов, которые можно захватить за один ход.

Если перемещение невозможно или у вас нет ни одного форта под вашим командованием, верните 0.

Примеры:
Ввод: forts = [1,0,0,-1,0,0,0,0,1]
Вывод: 4

Ввод: forts = [0,0,1,-1]
Вывод: 0
'''

from typing import List

def capture_forts(forts: List[int]) -> int:
    maximum_captured = 0
    last_non_zero_position = -1

    for current_position, current_value in enumerate(forts):
        if current_value != 0:
            if last_non_zero_position != -1:
                last_value = forts[last_non_zero_position]
                if last_value != current_value:
                    maximum_captured = max(
                        maximum_captured,
                        current_position - last_non_zero_position - 1
                    )
            last_non_zero_position = current_position

    return maximum_captured