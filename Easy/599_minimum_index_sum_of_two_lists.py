'''
Given two arrays of strings list_1 and list_2, find all the common strings that have the least index sum.
    + A common string is a string that appears in both list_1 and list_2.
    + The index sum of a common string is defined as i + j where i is the index of the string in list_1 and j is the index in list_2.
    + You need to find all common strings that achieve the minimum index sum among all possible common strings.

Return these strings in any order.

Examples:
Input: list_1 = ["Shogun","Tapioca Express","Burger King","KFC"], list_2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]

Input: list_1 = ["Shogun","Tapioca Express","Burger King","KFC"], list_2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]

Даны два массива строк list_1 и list_2. Необходимо найти все общие строки с минимальной суммой индексов.
    + Общая строка — это строка, которая встречается и в list_1, и в list_2.
    + Сумма индексов для общей строки определяется как i + j, где i — индекс этой строки в list_1, а j — индекс в list_2.
    + Нужно найти все общие строки, для которых эта сумма минимальна среди всех общих строк.

Вернуть можно в любом порядке.

Примеры:
Ввод: list_1 = ["Shogun","Tapioca Express","Burger King","KFC"], list_2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Вывод: ["Shogun"]

Ввод: list_1 = ["Shogun","Tapioca Express","Burger King","KFC"], list_2 = ["KFC","Shogun","Burger King"]
Вывод: ["Shogun"]
'''

from typing import List

def find_restaurant(list_1: List[str], list_2: List[str]) -> List[str]:
    index_map = {word: i for i, word in enumerate(list_1)}
    min_sum = float('inf')
    result = []
        
    for j, word in enumerate(list_2):
        if word in index_map:
            i = index_map[word]
            total_index = i + j
            if total_index < min_sum:
                min_sum = total_index
                result = [word]
            elif total_index == min_sum:
                result.append(word)
        
    return result