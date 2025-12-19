'''
You are given a string time of length 5, which represents the current time on a digital clock in the format "hh:mm".
    - The earliest valid time is "00:00";
    - The latest valid time is "23:59".

In the string time, some digits may be unknown and are represented by the character '?'.

Each '?' must be replaced with a digit from 0 to 9.

Return an integer representing the number of valid clock times that can be formed by replacing every '?' with a digit from 0 to 9, such that the resulting time is valid.

Examples:
Input: time = "?5:00"
Output: 2

Input: time = "0?:0?"
Output: 100

Дана строка time длины 5, которая представляет текущее время на цифровых часах в формате "hh:mm".
    - Минимально возможное время - "00:00";
    - Максимально возможное время - "23:59".

В строке time некоторые цифры могут быть неизвестны и обозначены символом '?'.

Каждый символ '?' необходимо заменить цифрой от 0 до 9.

Необходимо вернуть целое число — количество корректных вариантов времени, которые можно получить, заменив все символы '?' цифрами от 0 до 9, так чтобы полученное время было допустимым.

Примеры:
Ввод: time = "?5:00"
Вывод: 2

Ввод: time = "0?:0?"
Вывод: 100
'''

def count_time(time: str) -> int:
    hours_count = 1
    minutes_count = 1

    hours_first_digit = time[0]
    hours_second_digit = time[1]

    if hours_first_digit == '?' and hours_second_digit == '?':
        hours_count = 24
    elif hours_first_digit == '?':
        if int(hours_second_digit) <= 3:
            hours_count = 3
        else:
            hours_count = 2
    elif hours_second_digit == '?':
        if hours_first_digit == '2':
            hours_count = 4
        else:
            hours_count = 10

    minutes_first_digit = time[3]
    minutes_second_digit = time[4]

    if minutes_first_digit == '?' and minutes_second_digit == '?':
        minutes_count = 60
    elif minutes_first_digit == '?':
        minutes_count = 6
    elif minutes_second_digit == '?':
        minutes_count = 10

    return hours_count * minutes_count