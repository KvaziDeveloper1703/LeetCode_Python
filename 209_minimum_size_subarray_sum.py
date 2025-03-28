'''
You are given an array of positive integers nums and a positive integer target.
Find the minimal length of a contiguous subarray of which the sum is greater than or equal to target. If no such subarray exists, return 0.

Examples:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2

Input: target = 4, nums = [1,4,4]
Output: 1

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        total = 0
        min_length = float('inf')

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                min_length = min(min_length, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if min_length == float('inf') else min_length