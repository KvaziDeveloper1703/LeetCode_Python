'''
Write a function that finds the longest common prefix among an array of strings.
If there is no common prefix, return an empty string "".

Examples:
Input: strs = ["flower", "flow", "flight"]
Output: "fl"

Input: strs = ["dog", "racecar", "car"]
Output: ""

Напишите функцию, которая находит наибольший общий префикс среди массива строк.
Если общего префикса нет, верните пустую строку "".

Примеры:
Вход: strs = ["flower", "flow", "flight"]
Выход: "fl"

Вход: strs = ["dog", "racecar", "car"]
Выход: ""
'''

from typing import List

def longest_common_prefix(given_strings: List[str]) -> str:
        if not given_strings:
            return ""
        
        prefix = given_strings[0]

        for word in given_strings[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix