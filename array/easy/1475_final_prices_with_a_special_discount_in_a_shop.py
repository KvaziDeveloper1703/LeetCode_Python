'''
You are given an integer array prices, where prices[i] is the price of the i-th item in a shop.

There is a special discount:
    - If you buy the i-th item, you will receive a discount equal to prices[j], where j is the smallest index such that j > i and prices[j] <= prices[i];
    - If no such j exists, then you do not receive any discount.

Return an array answer, where answer[i] is the final price you pay for the i-th item after applying the discount.

Examples:
Input: prices = [8, 4, 6, 2, 3]
Output: [4, 2, 4, 2, 3]

Input: prices = [1, 2, 3, 4, 5]
Output: [1, 2, 3, 4, 5]

Дан массив целых чисел prices, где prices[i] - это цена i-го товара в магазине.

Существует специальная скидка:
    - Если вы покупаете i-й товар, вы получите скидку, равную prices[j], где j - минимальный индекс такой, что j > i и prices[j] <= prices[i];
    - Если такого j нет, скидка не предоставляется.

Верните массив answer, где answer[i] - это итоговая цена, которую вы заплатите за i-й товар с учётом скидки.

Примеры:
Ввод: prices = [8, 4, 6, 2, 3]
Вывод: [4, 2, 4, 2, 3]

Ввод: prices = [1, 2, 3, 4, 5]
Вывод: [1, 2, 3, 4, 5]
'''

from typing import List

def final_prices(prices: List[int]) -> List[int]:
    length = len(prices)
    answer = prices[:]

    for i in range(length):
        for j in range(i + 1, length):
            if prices[j] <= prices[i]:
                answer[i] = prices[i] - prices[j]
                break

    return answer