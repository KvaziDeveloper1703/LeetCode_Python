'''
Given an integer array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times in the array.
You can assume that the majority element always exists in the input array.

Examples:
Input: nums = [3, 2, 3]
Output: 3

Input: nums = [2, 2, 1, 1, 1, 2, 2]
Output: 2
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for number in nums:
            if count == 0:
                candidate = number
            count += 1 if number == candidate else -1

        return candidate