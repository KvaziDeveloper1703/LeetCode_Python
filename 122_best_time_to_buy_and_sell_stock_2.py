'''
You are given an integer array prices, where prices[i] represents the price of a given stock on the i‑th day.
On each day, you may choose to buy and/or sell the stock.
However, you can only hold at most one share at a time, meaning you must sell the stock before buying again.
You are allowed to buy and sell on the same day.

Return the maximum profit you can achieve.

Examples:
Input: prices = [7, 1, 5, 3, 6, 4]
Output: 7

Input: prices = [1, 2, 3, 4, 5]
Output: 4

Input: prices = [7, 6, 4, 3, 1]
Output: 0
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit