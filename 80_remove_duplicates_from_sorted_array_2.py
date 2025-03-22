'''
You are given a sorted integer array nums (in non-decreasing order). Modify the array in-place so that each unique element appears at most twice, while preserving the relative order of the elements.
Since it's not possible to change the size of the array in some programming languages, you should place the result in the first part of the array nums. More formally:
+ Let k be the number of elements after removing extra duplicates.
+ The first k elements of nums should contain the final result.
+ The remaining elements beyond the first k positions do not matter.

You must not use any extra space — the algorithm should run in-place with O(1) extra memory.
Return the value of k.

Examples:
Input: nums = [1, 1, 1, 2, 2, 3]
Output: 5, nums = [1, 1, 2, 2, 3, _]

Input: nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
Output: 7, nums = [0, 0, 1, 1, 2, 3, 3, _, _]
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        write_index = 2

        for read_index in range(2, len(nums)):
            if nums[read_index] != nums[write_index - 2]:
                nums[write_index] = nums[read_index]
                write_index += 1

        return write_index