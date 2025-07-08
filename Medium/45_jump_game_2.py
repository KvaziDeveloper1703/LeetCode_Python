'''
Given a 0-indexed array of integers numbers of length n. You start at the first element numbers[0]. Each element numbers[i] represents the maximum number of steps you can jump forward from index i. In other words, from index i, you can jump to any index in the range [i + 1, i + numbers[i]], as long as it is within bounds (i + j < n).
Return the minimum number of jumps required to reach the last index (numbers[n - 1]). You can assume that it is always possible to reach the last index.

Examples:
Input: numbers = [2, 3, 1, 1, 4]
Output: 2

Input: numbers = [2, 3, 0, 1, 4]
Output: 2

Дан массив целых чисел numbers длины n. Вы начинаете с первого элемента numbers[0]. Каждый элемент numbers[i] указывает максимальное количество шагов, которое вы можете сделать вперёд из позиции i. Другими словами, из индекса i вы можете прыгнуть на любой индекс в диапазоне [i + 1, i + numbers[i]], если он не выходит за границы массива (i + j < n).
Ваша задача — вернуть минимальное количество прыжков, необходимое, чтобы достичь последнего индекса (numbers[n - 1]). Можно считать, что до последнего индекса всегда можно добраться.

Примеры:
Ввод: numbers = [2, 3, 1, 1, 4]
Вывод: 2

Ввод: numbers = [2, 3, 0, 1, 4]
Вывод: 2
'''

from typing import List

def jump(numbers: List[int]) -> int:
    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(len(numbers) - 1):
        farthest = max(farthest, i + numbers[i])

        if i == current_end:
            jumps += 1
            current_end = farthest

    return jumps