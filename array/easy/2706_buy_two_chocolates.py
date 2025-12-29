'''
You are given an integer array prices, where each element represents the price of a chocolate in a store. You are also given an integer money, which represents the amount of money you initially have.

You must buy exactly two chocolates such that the amount of money left after the purchase is non-negative. Among all valid choices, you want to minimize the total cost of the two chocolates you buy.

Return the amount of money that remains after buying the two chocolates.

If it is not possible to buy two chocolates without exceeding your available money, return money.

Examples:
Input: prices = [1, 2, 2], money = 3
Output: 0

Input: prices = [3, 2, 3], money = 3
Output: 3

Дан целочисленный массив prices, где каждый элемент обозначает цену шоколада в магазине. Также дано целое число money, представляющее вашу начальную сумму денег.

Необходимо купить ровно два шоколада так, чтобы после покупки у вас осталось неотрицательное количество денег. Среди всех возможных вариантов нужно выбрать тот, при котором суммарная стоимость двух шоколадов минимальна.

Верните количество денег, которое останется у вас после покупки двух шоколадов.

Если невозможно купить два шоколада, не превысив имеющуюся сумму, верните значение money.

Примеры:
Ввод: prices = [1, 2, 2], money = 3
Вывод: 0

Ввод: prices = [3, 2, 3], money = 3
Вывод: 3
'''

from typing import List

def buy_choco(prices: List[int], money: int) -> int:
    prices.sort()
    total_cost = prices[0] + prices[1]

    if total_cost <= money:
        return money - total_cost

    return money