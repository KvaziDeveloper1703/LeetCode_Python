'''
Given a sorted array of characters letters, arranged in non-decreasing lexicographical order. The array contains at least two distinct characters. You are also given a target character target.

Return the smallest character in letters that is strictly greater than target. If there is no such character, return the first character in the array letters.

Examples:
Input: letters = ["c", "f", "j"], target = "a"
Output: "c"

Input: letters = ["c", "f", "j"], target = "c"
Output: "f"

Вам дан отсортированный массив символов letters в неубывающем лексикографическом порядке. Массив содержит как минимум два разных символа. Также дан символ target.

Ваша задача — вернуть наименьший символ из массива letters, который строго больше, чем target. Если такого символа нет, верните первый символ массива letters.

Примеры:
Ввод: letters = ["c", "f", "j"], target = "a"
Вывод: "c"

Ввод: letters = ["c", "f", "j"], target = "c"
Вывод: "f"
'''

from typing import List

def next_greatest_letter(letters: List[str], target: str) -> str:
    left, right = 0, len(letters) - 1

    while left <= right:
        middle = (left + right) // 2
        if letters[middle] <= target:
            left = middle + 1
        else:
            right = middle - 1

    return letters[left] if left < len(letters) else letters[0]