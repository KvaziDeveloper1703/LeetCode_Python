'''
You are given a 0-indexed array of strings details.

Each element in details represents information about a passenger and is encoded as a string of exactly 15 characters.

The encoding format is as follows:
    - The first 10 characters represent the passenger’s phone number;
    - The 11th character indicates the gender of the passenger;
    - The 12th and 13th characters represent the age of the passenger;
    - The last 2 characters represent the seat number assigned to the passenger.

Your task is to return the number of passengers whose age is strictly greater than 60.

Examples:
Input: details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
Output: 2

Input: details = ["1313579440F2036", "2921522980M5644"]
Output: 0

Вам дан массив строк с нулевой индексацией details.

Каждый элемент массива содержит информацию о пассажире, закодированную в виде строки длины 15 символов.

Формат строки следующий:
    - Первые 10 символов - номер телефона пассажира;
    - 11-й символ - пол пассажира;
    - 12-й и 13-й символы - возраст пассажира;
    - Последние 2 символа - номер места пассажира.

Необходимо вернуть количество пассажиров, возраст которых строго больше 60 лет.

Пример:
Ввод: details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
Вывод: 2

Ввод: details = ["1313579440F2036", "2921522980M5644"]
Вывод: 0
'''

from typing import List

def count_seniors(details: List[str]) -> int:
    seniors_count = 0

    for passenger_details in details:
        age = int(passenger_details[11:13])
        if age > 60:
            seniors_count += 1

    return seniors_count