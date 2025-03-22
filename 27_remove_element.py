'''
You are given an integer array nums and an integer val. Your task is to remove all occurrences of val from the array in-place. The relative order of the elements may change.
After removing all instances of val, return the number of elements that remain, denoted as k.

Requirements:
+ Modify the array nums in-place such that the first k elements are the elements not equal to val.
+ The remaining elements beyond index k - 1 do not matter — you can leave them as-is.
+ Return the value of k.

Examples:
Input: nums = [3, 2, 2, 3], val = 3
Output: 2, nums = [2, 2, _, _]

Input: nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
Output: 5, nums = [0, 1, 4, 0, 3, _, _, _]
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write_index = 0

        for read_index in range(len(nums)):
            if nums[read_index] != val:
                nums[write_index] = nums[read_index]
                write_index += 1

        return write_index