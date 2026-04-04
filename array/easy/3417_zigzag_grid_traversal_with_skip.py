'''
You are given an m x n 2D array grid of positive integers.
Traverse the grid in a zigzag pattern, while skipping every alternate cell.

Zigzag traversal rules:
    - Start at the top-left cell (0, 0);
    - Move right across the first row until the end;
    - Move down to the next row;
    - Then move left across that row until the beginning;
    - Continue alternating directions (right → left → right → …) for each row;
    - During traversal, visit only every second cell (skip alternate cells).

Return an array result containing the values of the visited cells in the order they are traversed.

Examples:
Input: grid = [[1,2],[3,4]]
Output: [1,4]

Input: grid = [[2,1],[2,1],[2,1]]
Output: [2,1,2]

Дан двумерный массив grid размером m x n, состоящий из положительных целых чисел.
Необходимо пройти по массиву в зигзагообразном порядке, при этом пропуская каждую вторую ячейку.

Правила обхода:
    - Начать с верхнего левого элемента (0, 0);
    - Двигаться вправо по первой строке до конца;
    - Затем перейти на следующую строку вниз;
    - Двигаться влево по этой строке до начала;
    - Продолжать чередовать направления (вправо → влево → вправо → …);
    - Во время обхода посещать только каждую вторую ячейку (пропуская остальные).

Верните массив result, содержащий значения посещённых элементов в порядке обхода.

Примеры:
Ввод: grid = [[1,2],[3,4]]
Вывод: [1,4]

Ввод: grid = [[2,1],[2,1],[2,1]]
Вывод: [2,1,2]
'''

from typing import List

def zigzag_traversal(grid: List[List[int]]) -> List[int]:
    res = []
    m = len(grid)
    n = len(grid[0])

    cnt = 0

    for i in range(m):
        if i % 2 == 0:
            cols = range(n)
        else:
            cols = range(n - 1, -1, -1)

        for j in cols:
            if cnt % 2 == 0:
                res.append(grid[i][j])
            cnt += 1

    return res