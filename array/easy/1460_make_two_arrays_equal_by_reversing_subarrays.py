'''
You are given two integer arrays target and arr of equal length.
In one step, you can select any non-empty subarray of arr and reverse it.
You can perform this operation any number of times.
Return true if it is possible to make arr equal to target. Otherwise, return false.

Examples:
Input: target = [1,2,3,4], arr = [2,4,1,3]
Output: true

Input: target = [7], arr = [7]
Output: true

Даны два целочисленных массива target и arr одинаковой длины.
За один шаг можно выбрать любой непустой подмассив массива arr и развернуть его.
Эту операцию можно выполнять любое количество раз.
Вернуть true, если можно преобразовать arr в target. Иначе вернуть false.

Примеры:
Ввод: target = [1,2,3,4], arr = [2,4,1,3]
Вывод: true

Ввод: target = [7], arr = [7]
Вывод: true
'''

from typing import List

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target_sorted = sorted(target)
        arr_sorted = sorted(arr)
        
        return target_sorted == arr_sorted