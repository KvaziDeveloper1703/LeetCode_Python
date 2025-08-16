'''
Given an integer array candies, where candies[i] is the number of candies the i-th kid has.

There is also an integer extraCandies, representing the number of additional candies you can give.

For each kid, check if giving all extraCandies to them will make their total number of candies greater than or equal to the maximum number of candies any kid has.

Return a boolean array result of length n, where result[i] = true if the i-th kid can have the greatest number of candies, otherwise false.

Examples:
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]

Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false]

Дан массив целых чисел candies, где candies[i] — количество конфет у i-го ребёнка.

Также дано число extraCandies, обозначающее количество дополнительных конфет, которые можно отдать.

Для каждого ребёнка нужно проверить: если отдать ему все extraCandies, станет ли его количество конфет не меньше максимального среди всех детей.

Нужно вернуть булев массив result длиной n, где result[i] = true, если i-й ребёнок может иметь наибольшее количество конфет, иначе false.

Примеры:
Ввод: candies = [2,3,5,1,3], extraCandies = 3
Вывод: [true,true,true,false,true]

Ввод: candies = [4,2,1,1,2], extraCandies = 1
Вывод: [true,false,false,false,false]
'''

from typing import List

def kids_with_candies(candies: List[int], extraCandies: int) -> List[bool]:
    max_candies = max(candies)
    result = []
    for candie in candies:
        result.append(candie + extraCandies >= max_candies)
    return result