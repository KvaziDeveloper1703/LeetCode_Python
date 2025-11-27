'''
A distinct string is a string that appears exactly once in an array.
You are given an array of strings array and an integer k.
Return the k-th distinct string in the order they appear in array.
If there are fewer than k distinct strings, return an empty string "".

Examples:
Input: array = ["d","b","c","b","c","a"], k = 2
Output: "a"

Input: array = ["aaa","aa","a"], k = 1
Output: "aaa"

Уникальная строка - это строка, которая появляется в массиве ровно один раз.
Дан массив строк array и число k.
Нужно вернуть k-тую уникальную строку в порядке появления в массиве.
Если уникальных строк меньше, чем k, вернуть пустую строку "".

Примеры:
Ввод: array = ["d","b","c","b","c","a"], k = 2
Вывод: "a"

Ввод: array = ["aaa","aa","a"], k = 1
Вывод: "aaa"
'''

from typing import List

def kth_distinct(array: List[str], k: int) -> str:
    frequency_by_string = {}
    for string in array:
        if string in frequency_by_string:
            frequency_by_string[string] += 1
        else:
            frequency_by_string[string] = 1

    distinct_strings_count = 0
    for string in array:
        if frequency_by_string[string] == 1:
            distinct_strings_count += 1
            if distinct_strings_count == k:
                return string

    return ""