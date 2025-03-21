"""
Given an array of integers nums, return the running sum of the array.

The running sum at index i is defined as the sum of all elements from index 0 to i, i.e.:
runningSum[i] = nums[0] + nums[1] + ... + nums[i]

Examples:
Input: nums = [1, 2, 3, 4]
Output: [1, 3, 6, 10]

Input: nums = [1, 1, 1, 1, 1]
Output: [1, 2, 3, 4, 5]

Input: nums = [3, 1, 2, 10, 1]
Output: [3, 4, 6, 16, 17]
"""

class Solution(object):
    def runningSum(self, nums):
        result = []
        current_sum = 0
        for number in nums:
            current_sum += number
            result.append(current_sum)
        return result