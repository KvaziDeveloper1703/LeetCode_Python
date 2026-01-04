'''
You are given a binary string s that contains at least one '1'.

You may rearrange the bits of the string in any order. Your goal is to form the maximum possible odd binary number that can be created using exactly the same bits.

Return a string representing the resulting maximum odd binary number.

Examples:
Input: s = "010"
Output: "001"

Input: s = "0101"
Output: "1001"

Вам дана двоичная строка s, которая содержит как минимум одну '1'.

Вы можете переставлять биты строки в любом порядке. Необходимо получить максимально возможное нечётное двоичное число, используя ровно те же самые биты.

Верните строку, представляющую максимальное нечётное двоичное число, которое можно получить.

Примеры:
Ввод: s = "010"
Вывод: "001"

Ввод: s = "0101"
Вывод: "1001"
'''

def maximum_odd_binary_number(s: str) -> str:
    ones_count = s.count("1")
    zeros_count = s.count("0")

    return "1" * (ones_count - 1) + "0" * zeros_count + "1"