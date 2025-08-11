'''
A binary watch has:
    + 4 LEDs to represent the hour (from 0 to 11),
    + 6 LEDs to represent the minutes (from 0 to 59).

Each LED can be either on (1) or off (0), with the least significant bit on the right.

Given an integer turned_on, representing the number of LEDs that are currently on.

Return all possible times the watch could represent with exactly turned_on LEDs lit. You can return the result in any order.

Formatting rules:
    + The hour must not have a leading zero (e.g., "1:00" is valid, but "01:00" is not).
    + The minute must always have two digits, with a leading zero if necessary (e.g., "10:02" is valid, but "10:2" is not).

Examples:
Input: turned_on = 1
Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]

Input: turned_on = 9
Output: []

Бинарные часы устроены так:
    + 4 светодиода (LED) отображают часы (от 0 до 11),
    + 6 светодиодов отображают минуты (от 0 до 59).

Каждый светодиод может быть включён (1) или выключен (0), при этом младшие биты — справа.

Дано целое число turned_on, обозначающее количество включённых светодиодов.

Нужно вернуть все возможные значения времени, которые могут быть показаны на часах при таком числе включённых светодиодов. Ответ можно вернуть в любом порядке.

Правила форматирования:
    + В часах не должно быть ведущих нулей (например, "1:00" допустимо, но "01:00" — нет).
    + В минутах всегда должно быть две цифры, ведущий ноль допустим (например, "10:02" — правильно, а "10:2" — нет).

Примеры:
Ввод: turned_on = 1
Вывод: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]

Ввод: turned_on = 9
Вывод: []
'''

from typing import List

def read_binary_watch(turned_on: int) -> List[str]:
    possible_times = []

    for hour in range(12):
        for minute in range(60):
            leds_in_hour = hour.bit_count()
            leds_in_minute = minute.bit_count()

            if leds_in_hour + leds_in_minute == turned_on:
                time_string = f"{hour}:{minute:02d}"
                possible_times.append(time_string)

    return possible_times