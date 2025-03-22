'''
You are given a 0-indexed array of integers nums of length n. You start at the first element nums[0].
Each element nums[i] represents the maximum number of steps you can jump forward from index i. In other words, from index i, you can jump to any index in the range [i + 1, i + nums[i]], as long as it is within bounds (i + j < n).
Your task is to return the minimum number of jumps required to reach the last index (nums[n - 1]).
You can assume that it is always possible to reach the last index.

Examples:
Input: nums = [2, 3, 1, 1, 4]
Output: 2

Input: nums = [2, 3, 0, 1, 4]
Output: 2
'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps