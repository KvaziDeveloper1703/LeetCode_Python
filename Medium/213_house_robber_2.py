'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money hidden. The houses are arranged in a circle, meaning the first and last houses are adjacent.
You cannot rob two adjacent houses, because they have security systems that will alert the police.
Given an integer array numbers where numbers[i] is the amount of money in the i-th house, return the maximum amount of money you can rob without triggering the alarm.

Examples:
Input: numbers = [2, 3, 2]
Output: 3

Input: numbers = [1, 2, 3, 1]
Output: 4

Вы — профессиональный грабитель, планирующий ограбление домов на улице. В каждом доме спрятано некоторое количество денег. Все дома расположены по кругу, то есть первый и последний дома являются соседями.
Вы не можете ограбить два соседних дома, иначе сработает система безопасности и вызовет полицию.
Вам дан массив целых чисел numbers, где numbers[i] — количество денег в i-ом доме. Верните максимальную сумму денег, которую можно ограбить без срабатывания сигнализации.

Примеры:
Ввод: numbers = [2, 3, 2]
Вывод: 3

Ввод: numbers = [1, 2, 3, 1]
Вывод: 4
'''

from typing import List

class Solution:
    def rob(self, house_money_list: List[int]) -> int:
        def rob_linear(houses: List[int]) -> int:
            if not houses:
                return 0
            if len(houses) == 1:
                return houses[0]
            
            max_robbed_money = [0] * len(houses)
            max_robbed_money[0] = houses[0]
            max_robbed_money[1] = max(houses[0], houses[1])
            
            for i in range(2, len(houses)):
                max_robbed_money[i] = max(max_robbed_money[i - 1], max_robbed_money[i - 2] + houses[i])
            return max_robbed_money[-1]

        total_houses = len(house_money_list)
        if total_houses == 0:
            return 0
        if total_houses == 1:
            return house_money_list[0]

        max_rob_excluding_first = rob_linear(house_money_list[1:])
        max_rob_excluding_last = rob_linear(house_money_list[:-1])

        return max(max_rob_excluding_first, max_rob_excluding_last)