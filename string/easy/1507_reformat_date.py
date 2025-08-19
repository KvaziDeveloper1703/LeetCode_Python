'''
Given a date string in the format Day Month Year, where:
    + Day ∈ {"1st", "2nd", "3rd", "4th", …, "30th", "31st"}
    + Month ∈ {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}
    + Year ∈ [1900, 2100]

Convert this date into the format YYYY-MM-DD, where:
    + YYYY is the 4-digit year
    + MM is the 2-digit month
    + DD is the 2-digit day

Examples:
Input: date = "20th Oct 2052"
Output: "2052-10-20"

Input: date = "6th Jun 1933"
Output: "1933-06-06"

Дана строка даты в формате Day Month Year, где:
    + Day ∈ {"1st", "2nd", "3rd", "4th", …, "30th", "31st"}
    + Month ∈ {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}
    + Year ∈ [1900, 2100]

Преобразуйте дату в формат YYYY-MM-DD, где:
    + YYYY — это 4-значный год
    + MM — это 2-значный месяц
    + DD — это 2-значный день

Примеры:
Ввод: date = "20th Oct 2052"
Вывод: "2052-10-20"

Ввод: date = "6th Jun 1933"
Вывод: "1933-06-06"
'''

from typing import List

def reformatDate(date: str) -> str:
    month_map = {
        "Jan": "01",
        "Feb": "02",
        "Mar": "03",
        "Apr": "04",
        "May": "05",
        "Jun": "06",
        "Jul": "07",
        "Aug": "08",
        "Sep": "09",
        "Oct": "10",
        "Nov": "11",
        "Dec": "12",
    }

    parts = date.split()
    day_part = parts[0]
    month_part = parts[1]
    year = parts[2]

    digits_in_day = []
    for character in day_part:
        if character.isdigit():
            digits_in_day.append(character)
    day_number = "".join(digits_in_day)
    if len(day_number) == 1:
        day_number = "0" + day_number

    month_number = month_map[month_part]

    formatted_date = year + "-" + month_number + "-" + day_number
    return formatted_date