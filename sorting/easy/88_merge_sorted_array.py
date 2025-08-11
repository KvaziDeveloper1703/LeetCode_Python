'''
You are given two integer arrays, numbers_1 and numbers_2, both sorted in non-decreasing order, and two integers, m and n, representing the number of valid elements in numbers_1 and numbers_2, respectively.
Your task is to merge numbers_2 into numbers_1 as one sorted array in-place.
    + numbers_1 has a length of m + n, where:
        + The first m elements contain the elements to be merged;
        + The last n elements are set to 0 and should be ignored.
    + number_2 has exactly n elements.

Requirements:
    + Merge numbers_2 into numbers_1, so that numbers_1 becomes a sorted array of size m + n.
    + Do not return the merged array — modify numbers_1 in-place.

Examples:
Input: numbers_1 = [1,2,3,0,0,0], m = 3, numbers_2 = [2,5,6], n = 3
Output: numbers_1 = [1,2,2,3,5,6]

У тебя есть два целых массива, numbers_1 и numbers_2, оба отсортированы в неубывающем порядке, а также два целых числа m и n, которые представляют количество валидных элементов в numbers_1 и numbers_2 соответственно.
Твоя задача — объединить numbers_2 в numbers_1, чтобы получить один отсортированный массив на месте (in-place).
    + Массив numbers_1 имеет длину m + n, где:
        + Первые m элементов содержат элементы для объединения;
        + Последние n элементов равны 0 и должны игнорироваться.
    + Массив numbers_2 содержит ровно n элементов.

Требования:
    + Объедини numbers_2 в numbers_1, чтобы numbers_1 стал отсортированным массивом длиной m + n.
    + Не возвращай новый массив — модифицируй numbers_1 на месте.

Примеры:
Ввод: numbers_1 = [1,2,3,0,0,0], m = 3, numbers_2 = [2,5,6], n = 3
Вывод: numbers_1 = [1,2,2,3,5,6]
'''

from typing import List

def merge(numbers_1: List[int], n: int, numbers_2: List[int], m: int) -> None:
    index_numbers_1 = n - 1
    index_numbers_2 = m - 1
    merge_position = n + m - 1

    while index_numbers_2 >= 0:
        if index_numbers_1 >= 0 and numbers_1[index_numbers_1] > numbers_2[index_numbers_2]:
            numbers_1[merge_position] = numbers_1[index_numbers_1]
            index_numbers_1 -= 1
        else:
            numbers_1[merge_position] = numbers_2[index_numbers_2]
            index_numbers_2 -= 1
        merge_position -= 1

    return None