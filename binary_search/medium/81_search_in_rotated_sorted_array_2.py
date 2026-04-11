'''
You are given an integer array nums sorted in non-decreasing order.

Before being passed to your function, nums is rotated at an unknown pivot index k (0 ≤ k < nums.length). After rotation, the array becomes: [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]].

Return true if target exists in nums, otherwise return false.

Conditions:
    - The array may contain duplicate values;
    - You should minimize the number of operations.

Examples:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Дан массив целых чисел nums, отсортированный в неубывающем порядке.

Перед передачей в функцию массив был повернут на неизвестный индекс k (0 ≤ k < длина массива). После поворота он имеет вид: [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]].

Вернуть true, если target присутствует в массиве nums, иначе вернуть false.

Условия:
    - В массиве могут быть дубликаты;
    - Необходимо минимизировать количество операций.

Примеры:
Ввод: nums = [2,5,6,0,0,1,2], target = 0
Вывод: true

Ввод: nums = [2,5,6,0,0,1,2], target = 3
Вывод: false
'''

from typing import List

def search(nums: List[int], target: int) -> bool:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return True

        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1

        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return False