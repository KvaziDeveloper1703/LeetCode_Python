'''
You have a long flowerbed represented by an integer array flowerbed, where:
    + 0 means the plot is empty.
    + 1 means the plot already has a flower planted.

Flowers cannot be planted in adjacent plots.
Given an integer n, determine if you can plant n new flowers in the flowerbed without violating the no-adjacent-flowers rule.

Return True if it is possible, otherwise return False.

Examples:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True

Input: flowerbed = [1,0,0,0,1], n = 2
Output: False

У вас есть длинная клумба, представленная массивом целых чисел flowerbed, где:
    + 0 означает, что участок пустой.
    + 1 означает, что на участке уже посажен цветок.

Цветы нельзя сажать на смежных участках.
Дано целое число n. Определите, можно ли посадить n новых цветов, не нарушая правило о том, что цветы не могут находиться на соседних участках.

Если можно, верните True, иначе — False.

Примеры:
Ввод: flowerbed = [1,0,0,0,1], n = 1
Вывод: True

Ввод: flowerbed = [1,0,0,0,1], n = 2
Вывод: False
'''

from typing import List

def can_place_flowers(flowerbed: List[int], n: int) -> bool:
    count = 0
    length = len(flowerbed)
        
    for i in range(length):
        if flowerbed[i] == 0:
            empty_left = (i == 0) or (flowerbed[i - 1] == 0)
            empty_right = (i == length - 1) or (flowerbed[i + 1] == 0)
                
            if empty_left and empty_right:
                flowerbed[i] = 1
                count += 1
                if count >= n:
                    return True
                        
    return count >= n