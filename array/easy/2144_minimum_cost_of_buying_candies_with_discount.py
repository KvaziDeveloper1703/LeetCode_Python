'''
A shop offers a discount: for every two candies you buy, you can get a third candy for free.

You may choose any candy as the free one, but only if its cost is less than or equal to the minimum cost of the two candies you paid for.

For example, if you buy candies costing 2 and 3, you may take the candy costing 1 for free, but you cannot take the candy costing 4.

Given a 0-indexed array cost where cost[i] is the price of the i-th candy, return the minimum total amount of money needed to buy all the candies.

Examples:
Input: cost = [1, 2, 3]
Output: 5

Input: cost = [6, 5, 7, 9, 2, 2]
Output: 23

Магазин проводит акцию: за каждые две купленные конфеты можно получить третью бесплатно.

Бесплатную конфету можно выбрать любую, но только в том случае, если её цена меньше или равна минимальной цене из двух купленных конфет.

Например, если покупают конфеты стоимостью 2 и 3, то можно бесплатно взять конфету за 1, но нельзя взять конфету за 4.

Дан массив cost, где cost[i] — стоимость i-й конфеты. Нужно вернуть минимальную сумму денег, которую придётся заплатить, чтобы забрать все конфеты.

Примеры:
Ввод: cost = [1, 2, 3]
Вывод: 5

Ввод: cost = [6, 5, 7, 9, 2, 2]
Вывод: 23
'''

from typing import List

def minimum_cost(cost: List[int]) -> int:
    cost.sort(reverse=True)
    total = 0

    for i in range(len(cost)):
        if i % 3 != 2:
            total += cost[i]

    return total