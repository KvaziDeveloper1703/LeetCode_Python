"""
You are given a 2D integer array accounts where accounts[i][j] represents the amount of money the i‑th customer has in the j‑th bank.
A customer's wealth is the sum of money they have in all their bank accounts.
Return the maximum wealth among all customers.

Examples:
Input: accounts = [[1, 2, 3], [3, 2, 1]]
Output: 6

Input: accounts = [[1, 5], [7, 3], [3, 5]]
Output: 10

Input: accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
Output: 17
"""

class Solution(object):
    def maximumWealth(self, accounts):
        max_wealth = 0
        for customer in accounts:
            current_wealth = sum(customer)

            if current_wealth > max_wealth:
                max_wealth = current_wealth

        return max_wealth