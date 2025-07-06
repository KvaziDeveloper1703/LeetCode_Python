'''
You are given two sorted arrays, nums1 and nums2, of sizes m and n respectively. Your task is to find the median of the merged sorted array formed by combining these two arrays.
The overall time complexity should be O(log(m + n)).

Example:
Input: nums1 = [1, 3], nums2 = [2]
Output: 2.00000

Даны два отсортированных массива nums1 и nums2 размеров m и n соответственно. Нужно найти медиану объединённого отсортированного массива, составленного из этих двух.
Алгоритм должен работать за время O(log(m + n)).

Пример:
Ввод: nums1 = [1, 3], nums2 = [2]
Вывод: 2.00000
'''

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        half_len = (m + n + 1) // 2
        
        low, high = 0, m
        while low <= high:
            i = (low + high) // 2
            j = half_len - i
            
            if i < m and nums2[j - 1] > nums1[i]:
                low = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                high = i - 1
            else:
                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return float(max_of_left)

                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0