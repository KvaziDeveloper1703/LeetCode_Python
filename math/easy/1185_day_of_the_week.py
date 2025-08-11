'''
Given a specific date, return the corresponding day of the week.
The input is provided as three integers: day, month, and year.

Return the result as one of the following strings: {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

Examples:
Input: day = 31, month = 8, year = 2019
Output: "Saturday"

Input: day = 18, month = 7, year = 1999
Output: "Sunday"

По заданной дате верните соответствующий день недели.
Входные данные заданы тремя числами: day (день), month (месяц) и year (год).

Верните результат в виде одной из строк: {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

Примеры:
Ввод: day = 31, month = 8, year = 2019
Вывод: "Saturday"

Ввод: day = 18, month = 7, year = 1999
Вывод: "Sunday"
'''

from typing import List

def day_of_the_week(day: int, month: int, year: int) -> str:
    weekday_names: List[str] = [
        "Sunday", "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday"
    ]

    month_offsets: List[int] = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]

    adjusted_year: int = year - 1 if month < 3 else year

    term_year = adjusted_year
    term_leap_4 = adjusted_year // 4
    term_leap_100 = adjusted_year // 100
    term_leap_400 = adjusted_year // 400
    term_month = month_offsets[month - 1]
    term_day = day

    weekday_index: int = (
        term_year
        + term_leap_4
        - term_leap_100
        + term_leap_400
        + term_month
        + term_day
    ) % 7

    return weekday_names[weekday_index]