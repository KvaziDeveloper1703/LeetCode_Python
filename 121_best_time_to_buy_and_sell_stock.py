'''
You are given an array prices, where prices[i] represents the price of a given stock on the i‑th day.
Your goal is to maximize your profit by choosing one day to buy a stock and a different future day to sell that stock.
Return the maximum profit you can achieve from this transaction.
If no profit can be made, return 0.

Examples:
Input: prices = [7, 1, 5, 3, 6, 4]
Output: 5

Example 2
Input: prices = [7, 6, 4, 3, 1]
Output: 0
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)

        return max_profit