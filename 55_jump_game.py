'''
You are given an integer array nums. You start at the first index of the array.
Each element in the array represents the maximum number of steps you can jump forward from that position.

Return true if you can reach the last index, otherwise return false.

Examples:
Input: nums = [2, 3, 1, 1, 4]
Output: true

Input: nums = [3, 2, 1, 0, 4]
Output: false
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for i, jump in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + jump)
            if max_reach >= len(nums) - 1:
                return True

        return True