'''
You are given a 0-indexed integer array numbers and an integer k.

Your task is to perform the following operation exactly k times in order to maximize your score:
    - Select an element m from the array numbers;
    - Remove the selected element m from the array;
    - Insert a new element with value m + 1 into the array;
    - Increase your score by m.

After performing the operation exactly k times, return the maximum possible score.

Examples:
Input: numbers = [1,2,3,4,5], k = 3
Output: 18

Input: numbers = [5,5,5], k = 2
Output: 11

Дан целочисленный массив numbers с индексацией от 0 и целое число k.

Необходимо выполнить следующую операцию ровно k раз, чтобы максимизировать итоговый счёт:
    - Выбрать элемент m из массива numbers;
    - Удалить выбранный элемент m из массива;
    - Добавить в массив новый элемент со значением m + 1;
    - Увеличить счёт на значение m.

После выполнения операции ровно k раз верните максимально возможный счёт.

Примеры:
Ввод: numbers = [1,2,3,4,5], k = 3
Вывод: 18

Ввод: numbers = [5,5,5], k = 2
Вывод: 11
'''

from typing import List

def maximize_sum(numbers: List[int], k: int) -> int:
    m = max(numbers)
    return k * m + (k * (k - 1)) // 2