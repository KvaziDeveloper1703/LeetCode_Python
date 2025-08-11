'''
Given a string date representing a Gregorian calendar date in the format YYYY-MM-DD.

Return the day number of the year for that date.

Examples:
Input: date = "2019-01-09"
Output: 9

Input: date = "2019-02-10"
Output: 41

Дана строка date, представляющая дату в григорианском календаре в формате YYYY-MM-DD.

Нужно вернуть порядковый номер дня в году для этой даты.

Примеры:
Ввод: date = "2019-01-09"
Вывод: 9

Ввод: date = "2019-02-10"
Вывод: 41
'''

def day_of_the_year(date: str) -> int:
    year, month, day = map(int, date.split('-'))
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29

    return sum(days_in_month[:month - 1]) + day