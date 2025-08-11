"""
You are given a 2D integer array accounts where accounts[i][j] represents the amount of money the i‑th customer has in the j‑th bank.
A customer's wealth is the sum of money they have in all their bank accounts.

Return the maximum wealth among all customers.

Examples:
Input: accounts = [ [1, 2, 3], 
                    [3, 2, 1]]
Output: 6

Input: accounts = [ [1, 5], 
                    [7, 3], 
                    [3, 5]]
Output: 10

Дан двумерный массив целых чисел accounts, где accounts[i][j] — это сумма денег, которую i-й клиент имеет в j-м банке.
Богатство клиента — это сумма всех его средств во всех банках.

Необходимо вернуть максимальное богатство среди всех клиентов.

Примеры:
Вход: accounts = [  [1, 2, 3],  
                    [3, 2, 1]]
Выход: 6

Вход: accounts = [  [1, 5],  
                    [7, 3],  
                    [3, 5]]
Выход: 10
"""

from typing import List

def maximum_wealth(accounts: List[List[int]]) -> int:
    maximum_total_wealth = 0

    for customer_accounts in accounts:
        customer_wealth = sum(customer_accounts)
        if customer_wealth > maximum_total_wealth:
            maximum_total_wealth = customer_wealth

    return maximum_total_wealth