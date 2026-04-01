'''
You are given a binary array nums and an integer k.
Return true if all 1s in the array are at least k positions away from each other. Otherwise, return false.
The distance between any two 1s must be at least k zeros between them.

Examples:
Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true

Input: nums = [1,0,0,1,0,1], k = 2
Output: false

Дан бинарный массив nums и целое число k.
Нужно вернуть true, если все единицы (1) в массиве находятся на расстоянии не менее k позиций друг от друга. В противном случае вернуть false.
Между любыми двумя 1 должно быть как минимум k нулей.

Примеры:
Ввод: nums = [1,0,0,0,1,0,0,1], k = 2
Вывод: true

Ввод: nums = [1,0,0,1,0,1], k = 2
Вывод: false
'''

from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_index = -1
        
        for index in range(len(nums)):
            if nums[index] == 1:
                if last_index != -1 and index - last_index - 1 < k:
                    return False
                last_index = index
        
        return True