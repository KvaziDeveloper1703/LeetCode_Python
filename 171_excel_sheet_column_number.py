'''
Given a string column_title that represents the column title as it appears in an Excel sheet, return its corresponding column number.
Excel column titles are labeled alphabetically similar to a base-26 number system:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28

Examples:
Input: column_title = "A"
Output: 1

Input: column_title = "AB"
Output: 28

Дана строка column_title, представляющая название столбца в Excel. Необходимо вернуть соответствующий номер столбца.
Названия столбцов в Excel устроены как система счисления с основанием 26, где:
A  → 1
B  → 2
C  → 3
...
Z  → 26
AA → 27
AB → 28

Примеры:
Ввод: column_title = "A"
Вывод: 1

Ввод: column_title = "AB"
Вывод: 28
'''

def title_to_number(column_title: str) -> int:
    result = 0
    for character in column_title:
        value = ord(character) - ord('A') + 1
        result = result * 26 + value
    return result