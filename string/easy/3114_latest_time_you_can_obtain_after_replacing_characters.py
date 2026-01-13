'''
You are given a string s representing a time in 12-hour format, where some digits are replaced with "?".

A 12-hour time is formatted as "HH:MM", where:
    - HH is between 00 and 11;
    - MM is between 00 and 59.

The earliest possible time is 00:00, and the latest possible time is 11:59.
You must replace every "?" in s with a digit so that the resulting time is valid and as late as possible.
Return the resulting string.

Examples:
Input: s = "1?:?4"
Output: "11:54"

Input: s = "0?:5?"
Output: "09:59"

Дана строка s, которая задаёт время в 12-часовом формате, где некоторые цифры заменены на "?".

Время в 12-часовом формате записывается как "HH:MM", где:
    - HH находится в диапазоне от 00 до 11;
    - MM находится в диапазоне от 00 до 59.

Самое раннее возможное время - 00:00, самое позднее - 11:59.
Нужно заменить все символы "?" в строке s на цифры так, чтобы полученное время было корректным и максимально поздним.
Верните получившуюся строку.

Примеры:
Ввод: s = "1?:?4"
Вывод: "11:54"

Ввод: s = "0?:5?"
Вывод: "09:59"
'''

def find_latest_time(s: str) -> str:
    time_characters = list(s)

    if time_characters[0] == "?":
        if time_characters[1] == "?" or time_characters[1] <= "1":
            time_characters[0] = "1"
        else:
            time_characters[0] = "0"

    if time_characters[1] == "?":
        if time_characters[0] == "1":
            time_characters[1] = "1"
        else:
            time_characters[1] = "9"

    if time_characters[3] == "?":
        time_characters[3] = "5"

    if time_characters[4] == "?":
        time_characters[4] = "9"

    return "".join(time_characters)