'''
Given an array prices where prices[i] is the price of a given stock on the i-th day.
Find the maximum profit you can achieve. You may complete as many transactions as you like with the following restrictions:
    + After you sell a stock, you cannot buy stock the next day.
    + You may not engage in multiple transactions simultaneously — you must sell the stock before you can buy again.

Examples:
Input: prices = [1, 2, 3, 0, 2]
Output: 3

Input: prices = [1]
Output: 0

Вам дан массив prices, где prices[i] — это цена акции в i-й день.
Ваша задача — найти максимальную прибыль, которую можно получить. Вы можете совершать неограниченное количество сделок, но с ограничениями:
    + После того как вы продали акцию, вы не можете купить акцию на следующий день — необходимо пропустить один день.
    + Нельзя выполнять несколько сделок одновременно — вы должны сначала продать, прежде чем снова покупать.

Примеры:
Ввод: prices = [1, 2, 3, 0, 2]
Вывод: 3

Ввод: prices = [1]
Вывод: 0
'''

from typing import List

def max_profit(prices: List[int]) -> int:
    if not prices:
        return 0

    n = len(prices)
    profit_holding_stock = -prices[0]
    profit_after_selling = 0
    profit_in_rest = 0

    for day in range(1, n):
        previous_profit_holding = profit_holding_stock
        previous_profit_selling = profit_after_selling
        previous_profit_resting = profit_in_rest

        profit_holding_stock = max(previous_profit_holding, previous_profit_resting - prices[day])
        profit_after_selling = previous_profit_holding + prices[day]
        profit_in_rest = max(previous_profit_resting, previous_profit_selling)

    return max(profit_after_selling, profit_in_rest)