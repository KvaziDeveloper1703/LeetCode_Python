'''
Given an array strings of n strings, all of the same length. These strings can be visualized as rows in a grid.

Delete the columns that are not sorted in lexicographical order from top to bottom. A column is sorted if each character is less than or equal to the character below it.
Return the number of columns that should be deleted.

Examples:
Input: strings = ["cba","daf","ghi"]
Output: 1

Input: strings = ["a","b"]
Output: 0

Вам дан массив строк strings из n строк, все строки одинаковой длины. Эти строки можно представить в виде строк таблицы.

Ваша задача — удалить те столбцы, которые не отсортированы в лексикографическом порядке сверху вниз. Столбец считается отсортированным, если каждый символ не больше следующего под ним.
Необходимо вернуть количество столбцов, которые нужно удалить.

Примеры:
Ввод: strs = ["cba","daf","ghi"]
Вывод: 1

Ввод: strs = ["a","b"]
Вывод: 0
'''

from typing import List

def min_deletion_size(strings: List[str]) -> int:
    rows, columns = len(strings), len(strings[0])
    delete_count = 0

    for column in range(columns):
        for row in range(1, rows):
            if strings[row][column] < strings[row - 1][column]:
                delete_count += 1
                break
    return delete_count