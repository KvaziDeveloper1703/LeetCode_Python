'''
Given an integer column_number, return its corresponding column title as it appears in an Excel sheet.

Excel columns are labeled as follows:
A -> 1  
B -> 2  
C -> 3  
...  
Z -> 26  
AA -> 27  
AB -> 28  

This system is similar to a base-26 number system, but instead of 0-25, it uses letters A-Z.

Examples:
Input: column_number = 1
Output: "A"

Input: column_number = 28
Output: "AB"

Дано целое число column_number. Верните название столбца, как оно отображается в Excel.

В Excel используется следующая система именования столбцов:
A -> 1  
B -> 2  
C -> 3  
...  
Z -> 26  
AA -> 27  
AB -> 28  

Это аналогично системе счисления по основанию 26, но используются буквы A–Z, а не цифры.

Примеры:
Ввод: column_number = 1
Вывод: "A"

Ввод: column_number = 28
Вывод: "AB"
'''

def convert_to_title(column_number: int) -> str:
    result = []

    while column_number > 0:
        column_number -= 1
        remainder = column_number % 26
        result.append(chr(ord('A') + remainder))
        column_number //= 26

    return ''.join(reversed(result))