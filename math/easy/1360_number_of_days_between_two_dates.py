'''
Write a program to calculate the number of days between two given dates.

The two dates are provided as strings in the format "YYYY-MM-DD".

Examples:
Input: date_1 = "2019-06-29", date_2 = "2019-06-30"
Output: 1

Input: date_1 = "2020-01-15", date_2 = "2019-12-31"
Output: 15

Напишите программу, которая вычисляет количество дней между двумя заданными датами.

Даты задаются в виде строк в формате "YYYY-MM-DD".

Примеры:
Ввод: date_1 = "2019-06-29", date_2 = "2019-06-30"
Вывод: 1

Ввод: date_1 = "2020-01-15", date_2 = "2019-12-31"
Вывод: 15
'''

from datetime import date

def days_between_dates(date_1: str, date_2: str) -> int:
    date_1 = date.fromisoformat(date_1)
    date_2 = date.fromisoformat(date_2)
    return abs((date_2 - date_1).days)