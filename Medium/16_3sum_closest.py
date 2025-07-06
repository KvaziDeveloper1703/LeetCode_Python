'''
Given an integer array nums of length n and an integer target, find three integers in nums such that their sum is closest to target.
Return the sum of the three integers.

Example:
Input: nums = [-1, 2, 1, -4], target = 1
Output: 2

Дан массив целых чисел nums длиной n и целое число target. Необходимо найти три числа в массиве, сумма которых наиболее близка к числу target.
Верните сумму этих трёх чисел.

Пример:
Ввод: nums = [-1, 2, 1, -4], target = 1
Вывод: 2
'''

def three_sum_closest(nums: list[int], target: int) -> int:
    nums.sort()
    closest_sum = float('inf')
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return current_sum
    return closest_sum