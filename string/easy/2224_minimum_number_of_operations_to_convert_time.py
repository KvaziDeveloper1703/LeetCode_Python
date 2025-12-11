'''
You are given two strings, current and correct, each representing a time in 24-hour format.

A 24-hour time is written as "HH:MM", where:
    - HH is between 00 and 23,
    - MM is between 00 and 59.

The earliest possible time is 00:00, and the latest is 23:59.

In one operation, you may increase the time current by 1, 5, 15, or 60 minutes.

You may perform as many operations as needed.

Your task is to return the minimum number of operations required to transform current into correct.

Examples:
Input: current = "02:30", correct = "04:35"
Output: 3

Input: current = "11:00", correct = "11:01"
Output: 1

Даны две строки - current и correct, каждая представляет время в 24-часовом формате.

24-часовой формат записывается как "HH:MM", где:
    - HH - от 00 до 23,
    - MM - от 00 до 59.

Самое раннее время - 00:00, самое позднее - 23:59.

За одну операцию можно увеличить время current на 1, 5, 15 или 60 минут.

Количество операций не ограничено.

Нужно вернуть минимальное количество операций, чтобы преобразовать current во время correct.

Примеры:
Ввод: current = "02:30", correct = "04:35"
Вывод: 3

Ввод: current = "11:00", correct = "11:01"
Вывод: 1
'''

def convert_time(current: str, correct: str) -> int:
    current_hours, current_minutes = map(int, current.split(":"))
    correct_hours, correct_minutes = map(int, correct.split(":"))

    difference_in_minutes = (correct_hours * 60 + correct_minutes) - (current_hours * 60 + current_minutes)
    operations_count = 0

    for step_in_minutes in [60, 15, 5, 1]:
        operations_count += difference_in_minutes // step_in_minutes
        difference_in_minutes %= step_in_minutes

    return operations_count