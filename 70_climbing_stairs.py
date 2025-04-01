'''
You are climbing a staircase. It takes n steps to reach the top.
Each time, you can either climb 1 step or 2 steps. In how many distinct ways can you climb to the top?

Examples:
Input:
n = 2
Output:
2

Input:
n = 3
Output:
3
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        prev2, prev1 = 1, 1

        for i in range(2, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        return prev1