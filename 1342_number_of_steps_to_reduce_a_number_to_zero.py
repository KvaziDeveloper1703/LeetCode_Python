"""
Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

Example 1:
Input: num = 14
Output: 6

Example 2:
Input: num = 8
Output: 4

Example 3:
Input: num = 123
Output: 12
"""

class Solution(object):
    def numberOfSteps(self, num):
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            steps += 1
        return steps