'''
Given two strings:
    + jewels represents the types of stones that are jewels;
    + stones represents the stones you have.

Each character in stones is a type of stone you own. You want to determine how many of the stones you have are also jewels.

Examples:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Input: jewels = "z", stones = "ZZ"
Output: 0

Даны две строки:
    + jewels — виды камней, которые считаются драгоценностями;
    + stones — камни, которые у вас есть.

Каждый символ строки stones представляет один из видов камней. Необходимо определить, сколько из этих камней являются драгоценностями.

Примеры:
Ввод: jewels = "aA", stones = "aAAbbbb"
Вывод: 3

Ввод: jewels = "z", stones = "ZZ"
Вывод: 0
'''

def number_of_jewels_in_stones(jewels: str, stones: str) -> int:
    jewel_set = set(jewels)

    count = 0

    for stone in stones:
        if stone in jewel_set:
            count += 1
    return count