'''
You are given a time string in the format "hh:mm", where some digits may be hidden and replaced with the character '?'.

A valid time must be between 00:00 and 23:59, inclusive.

Your task is to replace each '?' with a digit so that the resulting time is the latest possible valid time.

Return this latest valid time.

Дана строка времени в формате "hh:mm", где некоторые цифры могут быть скрыты и заменены символом '?'.

Корректное время должно находиться в диапазоне от 00:00 до 23:59 включительно.

Нужно заменить каждый символ '?' на цифру так, чтобы получившееся время было самым поздним возможным, но всё ещё оставалось корректным.

Верни это максимально позднее корректное время.
'''

def maximum_time(time: str) -> str:
    hour_first_digit, hour_second_digit, _, minute_first_digit, minute_second_digit = time

    if hour_first_digit == '?':
        if hour_second_digit != '?' and int(hour_second_digit) > 3:
            hour_first_digit = '1'
        else:
            hour_first_digit = '2'

    if hour_second_digit == '?':
        if hour_first_digit == '2':
            hour_second_digit = '3'
        else:
            hour_second_digit = '9'

    if minute_first_digit == '?':
        minute_first_digit = '5'

    if minute_second_digit == '?':
        minute_second_digit = '9'

    return hour_first_digit + hour_second_digit + ":" + minute_first_digit + minute_second_digit