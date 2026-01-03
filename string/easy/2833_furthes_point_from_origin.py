'''
You are given a string moves of length n consisting only of the characters 'L', 'R', and '_'.

This string represents your movement on a number line starting from the origin 0.

For each move i (0 ≤ i < n), you may choose one of the following actions:
    - Move to the left if moves[i] = 'L' or moves[i] = '_';
    - Move to the right if moves[i] = 'R' or moves[i] = '_'.

After performing all n moves, determine the maximum possible distance from the origin that you can reach.

Return this maximum distance.

Examples:
Input: moves = "L_RL__R"
Output: 3

Input: moves = "_R__LL_"
Output: 5

Дана строка moves длины n, состоящая только из символов 'L', 'R' и '_'.

Эта строка описывает ваше движение по числовой прямой, начиная из точки 0.

Для каждого шага i (0 ≤ i < n) можно выбрать одно из следующих действий:
    - Сдвинуться влево, если moves[i] = 'L' или moves[i] = '_';
    - Сдвинуться вправо, если moves[i] = 'R' или moves[i] = '_'.

После выполнения всех n шагов определите максимальное возможное расстояние от начала координат, до которого можно добраться.

Верните это максимальное расстояние.

Примеры:
Ввод: moves = "L_RL__R"
Вывод: 3

Ввод: moves = "_R__LL_"
Вывод: 5
'''

def furthest_distance_from_origin(moves: str) -> int:
    left = moves.count('L')
    right = moves.count('R')
    free = moves.count('_')

    return abs(right - left) + free