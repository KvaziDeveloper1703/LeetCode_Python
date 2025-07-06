'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
+ 0 <= a, b, c, d < n;
+ a, b, c, and d are distinct;
+ nums[a] + nums[b] + nums[c] + nums[d] == target.

You may return the answer in any order.

Example:
Input: nums = [1, 0, -1, 0, -2, 2], target = 0
Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

Дан массив целых чисел nums длиной n. Необходимо вернуть все уникальные кортежи [nums[a], nums[b], nums[c], nums[d]] такие, что:
+ 0 <= a, b, c, d < n;
+ a, b, c и d — различные индексы;
+ nums[a] + nums[b] + nums[c] + nums[d] == target.

Ответ можно вернуть в любом порядке.

Пример:
Ввод: nums = [1, 0, -1, 0, -2, 2], target = 0
Вывод: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
'''

def four_sum(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()
    result = []
    n = len(nums)
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left, right = j + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                if current_sum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
    return result