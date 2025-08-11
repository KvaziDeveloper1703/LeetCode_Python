'''
Write a function that finds the longest common prefix among an array of strings.
If there is no common prefix, return an empty string "".

Examples:
Input: strings = ["flower", "flow", "flight"]
Output: "fl"

Input: strings = ["dog", "racecar", "car"]
Output: ""

Напишите функцию, которая находит наибольший общий префикс среди массива строк.
Если общего префикса нет, верните пустую строку "".

Примеры:
Ввод: strings = ["flower", "flow", "flight"]
Выход: "fl"

Ввод: strings = ["dog", "racecar", "car"]
Выход: ""
'''

from typing import List

def longest_common_prefix(strings: List[str]) -> str:
    if not strings:
        return ""
        
    prefix = strings[0]

    for word in strings[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix