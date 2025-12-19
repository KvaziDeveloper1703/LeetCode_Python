'''
You are given two arrays of strings, event1 and event2, which represent two inclusive events that occur on the same day.
    - event1 = [startTime₁, endTime₁];
    - event2 = [startTime₂, endTime₂].

Each time is given in 24-hour format as "HH:MM".

A conflict occurs if the two events have a non-empty intersection, meaning that there exists at least one moment in time that belongs to both events.

Return True if there is a conflict between the two events; otherwise, return False.

Examples:
Input: event1 = ["01:15", "02:00"], event2 = ["02:00", "03:00"]
Output: True

Input: event1 = ["01:00", "02:00"], event2 = ["01:20", "03:00"]
Output: True

Даны два массива строк event1 и event2, которые представляют два включающих (inclusive) события, произошедших в один и тот же день.
    - event1 = [startTime₁, endTime₁]
    - event2 = [startTime₂, endTime₂]

Время задано в 24-часовом формате "HH:MM".

Конфликт возникает в том случае, если два события имеют непустое пересечение, то есть существует хотя бы один момент времени, который принадлежит обоим событиям.

Необходимо вернуть True, если между событиями есть конфликт, и False - в противном случае.

Примеры:
Ввод: event1 = ["01:15", "02:00"], event2 = ["02:00", "03:00"]
Вывод: True

Ввод: event1 = ["01:00", "02:00"], event2 = ["01:20", "03:00"]
Вывод: True
'''

from typing import List

def have_conflict(event1: List[str], event2: List[str]) -> bool:
    start_time_event1, end_time_event1 = event1
    start_time_event2, end_time_event2 = event2

    return not (end_time_event1 < start_time_event2 or end_time_event2 < start_time_event1)