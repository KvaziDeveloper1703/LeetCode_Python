'''
Write an algorithm to determine if a number n is a happy number.
A happy number is defined by the following process:
+ Starting with any positive integer, replace the number by the sum of the squares of its digits.
+ Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
+ Numbers that end in 1 are happy, while numbers that fall into a cycle (not including 1) are not.

Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true

Example 2:
Input: n = 2
Output: false
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        def get_sum_of_squares(num: int) -> int:
            return sum(int(digit) ** 2 for digit in str(num))

        seen_numbers = set()

        while n != 1:
            n = get_sum_of_squares(n)

            if n in seen_numbers:
                return False

            seen_numbers.add(n)

        return True