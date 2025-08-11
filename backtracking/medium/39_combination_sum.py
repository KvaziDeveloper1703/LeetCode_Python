'''
Given an array of distinct integers called candidates and an integer target.
Return all unique combinations of numbers from candidates that sum up exactly to target.
    + You may use each number from candidates an unlimited number of times;
    + Combinations are unique if the frequency of at least one number differs;
    + The combinations can be returned in any order;
    + It is guaranteed that the number of unique combinations for the given input is less than 150.

Дан массив уникальных целых чисел candidates и целое число target.
Нужно вернуть все уникальные комбинации чисел из candidates, сумма которых в точности равна target.
    + Каждое число из candidates можно использовать неограниченное количество раз;
    + Комбинации считаются уникальными, если хотя бы одно число используется разное количество раз;
    + Порядок возвращения комбинаций не имеет значения;
    + Гарантируется, что количество уникальных комбинаций не превышает 150 для любого входа.
'''

from typing import List

def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    result = []

    def backtrack(remaining, combo, start):
        if remaining == 0:
            result.append(list(combo))
            return
        elif remaining < 0:
            return

        for i in range(start, len(candidates)):
            combo.append(candidates[i])
            backtrack(remaining - candidates[i], combo, i)
            combo.pop()

    backtrack(target, [], 0)
    return result