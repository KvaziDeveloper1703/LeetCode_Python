'''
You are given a string date representing a Gregorian calendar date in the format "yyyy-mm-dd".

You need to convert this date into its binary representation using the following rules:
    - Convert the year, month, and day to binary;
    - Write each part without leading zeros;
    - Combine them back in the format: year-month-day.

Return the binary representation of date.

Examples:
Input: date = "2080-02-29"
Output: "100000100000-10-11101"

Input: date = "1900-01-01"
Output: "11101101100-1-1"

Дана строка date, которая задаёт дату по григорианскому календарю в формате "yyyy-mm-dd".

Нужно преобразовать эту дату в её двоичное представление по правилам:
    - Перевести год, месяц и день в двоичную систему;
    - Записывать каждую часть без ведущих нулей;
    - Объединить их обратно в формате: год-месяц-день.

Верните двоичную запись даты date.

Примеры:
Ввод: date = "2080-02-29"
Вывод: "100000100000-10-11101"

Ввод: date = "1900-01-01"
Вывод: "11101101100-1-1"
'''

def convert_date_to_binary(date: str) -> str:
    year_string, month_string, day_string = date.split("-")

    year_number = int(year_string)
    month_number = int(month_string)
    day_number = int(day_string)

    year_binary = bin(year_number)[2:]
    month_binary = bin(month_number)[2:]
    day_binary = bin(day_number)[2:]

    return f"{year_binary}-{month_binary}-{day_binary}"