'''
You are given an integer array coins representing coins of different denominations, and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Examples:
Input: coins = [1, 2, 5], amount = 11
Output: 3

Input: coins = [2], amount = 3
Output: -1

Вам дан массив целых чисел coins, представляющий номиналы монет, и целое число amount, представляющее общую сумму денег.
Найдите наименьшее количество монет, необходимое для составления этой суммы.
Если невозможно набрать такую сумму с помощью данных монет, верните -1.
Можно считать, что каждой монеты доступно бесконечно много.

Примеры:
Ввод: coins = [1, 2, 5], amount = 11
Вывод: 3

Ввод: coins = [2], amount = 3
Вывод: -1
'''

def coin_сhange(self, coins: List[int], amount: int) -> int:
    min_number_of_coins = [float('inf')] * (amount + 1)
    min_number_of_coins[0] = 0

    for current_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= current_amount:
                min_number_of_coins[current_amount] = min(
                    min_number_of_coins[current_amount],
                    min_number_of_coins[current_amount - coin] + 1
                )

    if min_number_of_coins[amount] != float('inf'):
        return min_number_of_coins[amount]
    else:
        return -1