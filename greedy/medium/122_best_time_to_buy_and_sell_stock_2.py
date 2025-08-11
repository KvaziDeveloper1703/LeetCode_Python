'''
You are given an integer array prices, where prices[i] represents the price of a given stock on the i‑th day. On each day, you may choose to buy and/or sell the stock.
However, you can only hold at most one share at a time, meaning you must sell the stock before buying again. You are allowed to buy and sell on the same day.

Return the maximum profit you can achieve.

Examples:
Input: prices = [7, 1, 5, 3, 6, 4]
Output: 7

Input: prices = [1, 2, 3, 4, 5]
Output: 4

Дан массив целых чисел prices, где prices[i] — это цена акции в i-й день. Каждый день вы можете покупать и/или продавать акции.
Однако вы можете держать не более одной акции одновременно, то есть перед тем как купить новую акцию, вы должны продать текущую. Разрешено покупать и продавать акцию в один и тот же день.

Верните максимальную прибыль, которую можно получить.

Примеры:
Ввод: prices = [7, 1, 5, 3, 6, 4]
Вывод: 7

Ввод: prices = [1, 2, 3, 4, 5]
Вывод: 4
'''

from typing import List

def max_profit(prices: List[int]) -> int:
    total_profit = 0

    for day in range(1, len(prices)):
        if prices[day] > prices[day - 1]:
            daily_profit = prices[day] - prices[day - 1]
            total_profit += daily_profit

    return total_profit