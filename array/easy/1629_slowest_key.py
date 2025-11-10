'''
A newly designed keypad was tested by pressing a sequence of n keys, one at a time.

You are given:
- a string keys_pressed of length n, where keys_pressed[i] is the i-th key pressed;
- a list release_times, where release_times[i] is the time (in milliseconds) when the i-th key was released.

Both arrays are 0-indexed.
- The 0th key was pressed at time 0.
- Each subsequent key was pressed exactly when the previous one was released.

The duration of each keypress is defined as:
- release_times[0] for the first key,
- release_times[i] - release_times[i - 1] for all other keys.

You must return the key that had the longest duration.

If multiple keys have the same longest duration, return the lexicographically largest one.

Тестировалась новая клавиатура, на которой последовательно нажимались n клавиш.

Дано:
- строка keys_pressed длиной n, где keys_pressed[i] - это клавиша, нажатая i-м по счёту;
- список release_times, где release_times[i] - момент времени (в миллисекундах), когда i-я клавиша была отпущена.

Обе последовательности индексируются с нуля:
- Первая клавиша (0-я) была нажата в момент времени 0;
- Каждая следующая клавиша нажималась ровно в тот момент, когда предыдущая отпускалась.

Длительность каждого нажатия:
- для первой клавиши: release_times[0];
- для остальных: release_times[i] - release_times[i - 1].

Нужно вернуть символ клавиши, нажатие которой длилось дольше всех.

Если таких клавиш несколько, вернуть лексикографически наибольшую.
'''

from typing import List

def slowest_key(release_times: List[int], keys_pressed: str) -> str:
    max_duration = release_times[0]
    slowest_key = keys_pressed[0]

    for i in range(1, len(release_times)):
        duration = release_times[i] - release_times[i - 1]
        if duration > max_duration or (duration == max_duration and keys_pressed[i] > slowest_key):
            max_duration = duration
            slowest_key = keys_pressed[i]

    return slowest_key