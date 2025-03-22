'''
You are given a sorted integer array nums in non-decreasing order. Your task is to remove duplicates in-place so that each unique element appears only once, and the relative order of the elements is preserved.
After removing the duplicates, return the number of unique elements, denoted as k.

Requirements:
+ Modify the array nums in-place so that the first k elements contain the unique elements in their original order.
+ The remaining elements beyond index k - 1 do not matter — you can leave them as-is.
+ Return the value of k.

Examples:
Input: nums = [1, 1, 2]
Output: 2, nums = [1, 2, _]

Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
Output: 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        write_index = 1

        for read_index in range(1, len(nums)):
            if nums[read_index] != nums[write_index - 1]:
                nums[write_index] = nums[read_index]
                write_index += 1

        return write_index