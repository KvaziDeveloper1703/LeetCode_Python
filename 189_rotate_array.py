'''
Given an integer array nums, rotate the array to the right by k steps, where k is a non-negative integer.
The rotation should be done in-place, meaning you should modify the input array directly without using extra space for another array.

Examples:
Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
Output: [5, 6, 7, 1, 2, 3, 4]

Input: nums = [-1, -100, 3, 99], k = 2
Output: [3, 99, -1, -100]
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        def reverse_part(start: int, end: int):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse_part(0, n - 1)
        reverse_part(0, k - 1)
        reverse_part(k, n - 1)