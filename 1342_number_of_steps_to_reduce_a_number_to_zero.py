"""
Given an integer num, return the number of steps required to reduce it to zero.

You must follow these rules:
+ If the current number is even, divide it by 2.
+ If the current number is odd, subtract 1 from it.

Repeat the process until the number becomes 0, and return the total number of steps taken.

Examples:
Input: num = 14
Output: 6

Input: num = 8
Output: 4

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