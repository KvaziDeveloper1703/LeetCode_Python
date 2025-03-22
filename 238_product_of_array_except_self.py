'''
Given an integer array nums, return a new array answer such that answer[i] is equal to the product of all elements in nums except nums[i].
+ The result for each position must be calculated without using the division operation.
+ The algorithm must run in O(n) time complexity.
+ It is guaranteed that the product of all prefix or suffix elements will fit within a 32-bit integer.

Examples:
Input: nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]

Input: nums = [-1, 1, 0, -3, 3]
Output: [0, 0, 9, 0, 0]
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        answer = [1] * N

        left_product = 1
        for i in range(N):
            answer[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(N - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer