'''
You are given n balloons, indexed from 0 to n - 1. Each balloon has a number on it, given in the array nums.
Your task is to burst all the balloons in such an order that you maximize the total coins collected.
When you burst the i-th balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins.
    + If i - 1 or i + 1 is out of bounds, treat the value as 1 (as if there's a balloon with number 1).

Return the maximum number of coins you can collect by bursting the balloons wisely.

Examples:
Input: nums = [3,1,5,8]
Output: 167

Input: nums = [1,5]
Output: 10

Вам даны n воздушных шариков, пронумерованных от 0 до n - 1. На каждом шарике написано число — они представлены в массиве nums.
Ваша задача — лопнуть все шарики в таком порядке, чтобы максимизировать количество полученных монет.
Когда вы лопаете i-й шарик, вы получаете nums[i - 1] * nums[i] * nums[i + 1] монет.
    + Если i - 1 или i + 1 выходит за границы массива, считается, что там стоит 1.

Верните максимальное число монет, которое можно собрать, разумно выбирая порядок лопания шариков.

Примеры:
Ввод: nums = [3,1,5,8]
Вывод: 167

Ввод: nums = [1,5]
Вывод: 10
'''

from typing import List

class Solution:
    def maxCoins(self, balloon_values: List[int]) -> int:
        extended_values = [1] + balloon_values + [1]
        total_balloons = len(extended_values)
        max_coins_dp = [[0] * total_balloons for _ in range(total_balloons)]

        for interval_length in range(2, total_balloons):
            for left_index in range(0, total_balloons - interval_length):
                right_index = left_index + interval_length
                for last_burst_index in range(left_index + 1, right_index):
                    coins_gained = (
                        extended_values[left_index] *
                        extended_values[last_burst_index] *
                        extended_values[right_index]
                    )
                    coins_gained += (
                        max_coins_dp[left_index][last_burst_index] +
                        max_coins_dp[last_burst_index][right_index]
                    )
                    max_coins_dp[left_index][right_index] = max(
                        max_coins_dp[left_index][right_index],
                        coins_gained
                    )

        return max_coins_dp[0][total_balloons - 1]